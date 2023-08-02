def init_models() -> None:
    # import models here
    from bot.users.models import TelegramUser, TelegramUserRole
    from bot.CRM.models import Order, ProductInOrder