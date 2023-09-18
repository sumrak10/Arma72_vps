from typing import Optional

from pydantic import BaseModel
from fastapi import WebSocket



class WSRoom(BaseModel):
    uid: str
    ws: WebSocket
    id: int | None
    name: str | None
    message_id: int
    text: str

    class Config:
        arbitrary_types_allowed=True