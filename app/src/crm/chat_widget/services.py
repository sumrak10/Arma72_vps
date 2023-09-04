from typing import List

from fastapi import WebSocket

from .schemas import WSRoom
from .bot_funcs import invite_manager_in_room, send_message_to_manager


class WebSocketService:
    def __init__(self) -> None:
        self.rooms: List[WSRoom] = []

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
    
    async def disconnect(self, ws: WebSocket) -> None:
        wsroom = self.get_WSRoom_by_websocket(ws)
        self.rooms.remove(wsroom)
        send_message_to_manager(wsroom.id, "Онлайн консультация завершена клиентом.")
    
    async def set_manager_to_room(self, uid: str, manager_id: int) -> None:
        wsroom: WSRoom = self.get_WSRoom_by_uid(uid)
        wsroom.id = manager_id
        wsroom.ws.send_json({
            "command":"room_created"
        })

    async def direct(self, data:dict, ws:WebSocket) -> None:
        if data['command'] == 'first_message':
            self.rooms.append(WSRoom(uid=data['uid'], ws=ws, id=0))
            invite_manager_in_room(data['text'])
    

    #utils
    async def get_WSRoom_by_websocket(self, websocket:WebSocket) -> WSRoom:
        for wsroom in self.rooms:
            if wsroom.ws == websocket:
                return wsroom
    async def get_WSRoom_by_uid(self, uid:str) -> WSRoom:
        for wsroom in self.rooms:
            if wsroom.uid == uid:
                return wsroom

ws_service = WebSocketService()