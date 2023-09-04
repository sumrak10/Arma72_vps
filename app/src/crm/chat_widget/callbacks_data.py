from fastapi import WebSocket
from aiogram.filters.callback_data import CallbackData


class WSCallbackData(CallbackData, prefix="enter_the_consultation"):
    uid: str