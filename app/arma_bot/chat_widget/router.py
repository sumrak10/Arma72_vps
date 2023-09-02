from fastapi import APIRouter, WebSocket



router = APIRouter(
    prefix='chat_widget'
)

@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")