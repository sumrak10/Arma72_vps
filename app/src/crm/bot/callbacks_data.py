from aiogram.filters.callback_data import CallbackData as AbstractCallbackData

class CallbackData(AbstractCallbackData):
    fid: str

my_mails_callback_data = CallbackData(fid="my_mails")