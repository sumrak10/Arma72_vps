from pydantic import BaseModel
from fastapi import WebSocket



class WSRoom(BaseModel):
    uid: str
    ws: WebSocket
    id: int | None