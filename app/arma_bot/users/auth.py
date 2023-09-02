from aiogram import types

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from arma_bot.database.accessor import async_session_maker
from .models import TelegramUser, TelegramUserRole

async def get_current_user(msg: types.Message) -> TelegramUser:
    async with async_session_maker() as session:
        user = await session.get(TelegramUser, msg.from_user.id)
    if user is None:
        user = await register_user(msg)
    return user

async def register_user(msg: types.Message) -> TelegramUser:
    async with async_session_maker() as session:
        role = await session.get(TelegramUserRole, 1)
        user = TelegramUser(
            id = msg.from_user.id,
            first_name = msg.from_user.first_name,
            last_name = msg.from_user.last_name if msg.from_user.last_name is not None else '',
            role = role
        )
        session.add(user)
        await session.commit()
    return user