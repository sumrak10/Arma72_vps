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
        wsroom = self.get_WSRoom_by_websocket(ws)
        self.rooms.remove(wsroom)
        await send_message_to_manager(wsroom.id, "Онлайн консультация завершена клиентом.")
    
    async def set_manager_to_room(self, uid: str, manager_id: int) -> None:
        wsroom: WSRoom = self.get_WSRoom_by_uid(uid)
        wsroom.id = manager_id
        wsroom.ws.send_json({
            "command":"room_created"
        })

    async def direct(self, data:dict, ws:WebSocket) -> bool:
        logging.warn(msg="Getted new message")
        if data['command'] == 'first_message':
            self.rooms.append(WSRoom(uid=data['uid'], ws=ws, id=0))
            await invite_manager_in_room(data['uid'], data['text'])
    
        return True

    #utils
    def get_WSRoom_by_websocket(self, websocket:WebSocket) -> WSRoom:
        for wsroom in self.rooms:
            if wsroom.ws == websocket:
                return wsroom
    def get_WSRoom_by_uid(self, uid:str) -> WSRoom:
        for wsroom in self.rooms:
            if wsroom.uid == uid:
                return wsroom

ws_service = WebSocketService()