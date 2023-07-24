from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..users.models import TelegramUser


async def buildMainMenuKeyBoard(user: TelegramUser):
    rights = await user.get_role_rights()
    print(rights)
    mainMenuKeyboard = InlineKeyboardMarkup(row_width=10)
    mainMenuKeyboard.add(InlineKeyboardButton('Узнать статус заказа ✅', callback_data='mainMenu_send'))

    mainMenuKeyboard.add(InlineKeyboardButton('Настройки ⚙️', callback_data='mainMenu_settings'))
    return mainMenuKeyboard