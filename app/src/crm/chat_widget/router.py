import json

from fastapi import APIRouter, WebSocket
from fastapi.websockets import WebSocketDisconnect

from .services import ws_service



router = APIRouter(
    prefix='/chat_widget'
)


@router.websocket("/ws")
async def chat_widget_websocket(websocket: WebSocket):
    status = await ws_service.connect(websocket)
    try:
        while status:
            status = await ws_service.direct(
                data = await websocket.receive_json(mode="text"), 
                ws = websocket
            )
    except WebSocketDisconnect:
        await ws_service.disconnect(websocket)