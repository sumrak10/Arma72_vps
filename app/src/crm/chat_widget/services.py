from typing import List
import logging

from fastapi import WebSocket

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
        self.rooms.remove(wsroom)
        await send_message_to_manager(wsroom.id, "Онлайн консультация завершена клиентом.")
    
    async def close_ws_by_manager(self, manager_id: int) -> None:
        wsroom: WSRoom = self.get_WSRoom_by_manager_id(manager_id)
        if wsroom is None:
            return None
        await wsroom.ws.close()
        self.rooms.remove(wsroom)
        await send_message_to_manager(manager_id, "Онлайн консультация завершена.")

    async def set_manager_to_room(self, uid: str, manager_id: int) -> bool:
        wsroom: WSRoom = self.get_WSRoom_by_uid(uid)
        if wsroom is None:
            return False
        if wsroom.id != 0:
            return False
        wsroom.id = manager_id
        return True

    async def send_message_from_manager(self, manager_id: int, text:str, wsroom: WSRoom = None) -> None:
        if wsroom is None:
            wsroom: WSRoom = self.get_WSRoom_by_manager_id(manager_id)
        await wsroom.ws.send_json({
            "command": "message",
            'text': text
        })

    async def direct(self, data:dict, ws:WebSocket) -> bool:
        logging.warn(msg="Getted new message")

        if data['command'] == 'first_message':
            self.rooms.append(WSRoom(uid=data['uid'], ws=ws, id=0))
            await invite_manager_in_room(data['uid'], data['text'])

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


ws_service = WebSocketService()