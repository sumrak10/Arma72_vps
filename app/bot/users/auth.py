from aiogram import types

from .models import TelegramUser, TelegramUserRole

async def get_current_user(msg: types.Message) -> TelegramUser:
    user = await TelegramUser.query.where(TelegramUser.id==msg.from_user.id).gino.first()
    if user is None:
        default_role = await TelegramUserRole.query.where(TelegramUserRole.name=="client").gino.first()
        last_name = msg.from_user.last_name if msg.from_user.last_name is not None else ''
        user = await TelegramUser.create(
            id = msg.from_user.id,
            first_name = msg.from_user.first_name,
            last_name = last_name,
            role = default_role.id
        )
    return user