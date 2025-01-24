from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from Bot.config.config import HELP_URL
def article_button():
    keyborad=[
        [
            InlineKeyboardButton(text='Получить данные по товару',callback_data='get_article')
        ]
    ]
    btn=InlineKeyboardMarkup(inline_keyboard=keyborad)
    return btn

def help_found_article():
    keyboard=[
        [
            InlineKeyboardButton(text='Как получить артикул',url=HELP_URL)
        ]
    ]
    btn=InlineKeyboardMarkup(inline_keyboard=keyboard)
    return btn