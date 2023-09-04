from typing import Optional

from pydantic import BaseModel
from fastapi import WebSocket



class WSRoom(BaseModel):
    uid: str
    ws: WebSocket
    id: int

    class Config:
        arbitrary_types_allowed=True