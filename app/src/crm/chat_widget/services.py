from typing import List
import logging
import string
import random

from fastapi import WebSocket

from . import exceptions
from .._bot import bot
from ..config import settings
from .schemas import WSRoom
from .bot_funcs import invite_manager_in_room, send_message_to_manager


class WebSocketService:
    def __init__(self) -> None:
        self.rooms: List[WSRoom] = []

    async def connect(self, ws: WebSocket) -> bool:
        await ws.accept()
        return True
    
    async def disconnect(self, ws: WebSocket) -> None:
        logging.warn("WS disconnected")
        wsroom = self.get_WSRoom_by_websocket(ws)
        if wsroom is not None:
            self.rooms.remove(wsroom)
            manager_name = wsroom.name
            emoji = "✅"
            if manager_name is None:
                manager_name = "Отсутствовал"
                emoji = "💤"
            await bot.edit_message_text(
                text=f"{emoji} Консультация завершена клиентом\n❔ Текст запроса:{wsroom.text}\nⓂ️ Менеджер: {manager_name}",
                chat_id=settings.GROUP_ID,
                message_id=wsroom.message_id
            )
            if wsroom.id is not None:
                await send_message_to_manager(
                    wsroom.id, 
                    "✅ Онлайн консультация завершена клиентом."
                )
    
    async def close_ws_by_manager(self, manager_id: int) -> bool:
        wsroom: WSRoom = self.get_WSRoom_by_manager_id(manager_id)
        if wsroom is None:
            await send_message_to_manager(manager_id, "❌ Вы не в онлайн консультации.")
        else:
            await bot.edit_message_text(
                text=f"✅ Консультация завершена менеджером\n❔ Текст запроса:{wsroom.text}\nⓂ️ Менеджер: {wsroom.name}",
                chat_id=settings.GROUP_ID,
                message_id=wsroom.message_id
            )
            await wsroom.ws.close()
            self.rooms.remove(wsroom)
            await send_message_to_manager(manager_id, "✅ Онлайн консультация завершена Вами.")

    async def set_manager_to_room(self, 
        uid: str, 
        manager_id: int, 
        manager_name: str
    ) -> WSRoom:
        wsroom: WSRoom = self.get_WSRoom_by_uid(uid)
        if self.get_WSRoom_by_manager_id(manager_id) is not None:
            raise exceptions.UserNowInOtherRoom()
        if wsroom is None:
            raise exceptions.RoomNotFound()
        if wsroom.id is not None:
            raise exceptions.OtherManagerConnecteRoom()
        await send_message_to_manager(manager_id, text="🌀 Онлайн консультация начата")
        wsroom.id = manager_id
        wsroom.name = manager_name
        return wsroom

    async def send_message_from_manager(self, 
        manager_id: int, 
        text:str, 
        wsroom: WSRoom = None
    ) -> None:
        if wsroom is None:
            wsroom: WSRoom = self.get_WSRoom_by_manager_id(manager_id)
        await wsroom.ws.send_json({
            "command": "message",
            'text': text
        })

    async def direct(self, data:dict, ws:WebSocket) -> bool:

        if data['command'] == 'first_message':
            uid = self.generate_random_string(16)
            msg = await invite_manager_in_room(uid, data['text'])
            self.rooms.append(
                WSRoom(
                    uid=uid, 
                    ws=ws, 
                    id=None, 
                    name=None,
                    message_id=msg.message_id,
                    text=data['text']
                )
            )

        elif data['command'] == 'message':
            wsroom: WSRoom = self.get_WSRoom_by_websocket(ws)
            await send_message_to_manager(wsroom.id, data['text'])

        return True



    #utils
    def manager_now_in_consultation(self, id: int) -> bool:
        for wsroom in self.rooms:
            if wsroom.id == id:
                return True
        return False

    def get_WSRoom_by_websocket(self, websocket:WebSocket) -> WSRoom | None:
        for wsroom in self.rooms:
            if wsroom.ws == websocket:
                return wsroom

    def get_WSRoom_by_uid(self, uid:str) -> WSRoom | None:
        for wsroom in self.rooms:
            if wsroom.uid == uid:
                return wsroom

    def get_WSRoom_by_manager_id(self, id:int) -> WSRoom | None:
        for wsroom in self.rooms:
            if wsroom.id == id:
                return wsroom
            
    def generate_random_string(self, length) -> str:
        letters_and_digits = string.ascii_letters + string.digits
        crypt_rand_string = ''.join(random.choice(letters_and_digits) 
            for i in range(length))
        return crypt_rand_string


ws_service = WebSocketService()