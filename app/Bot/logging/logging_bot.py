# import from library aiogram
from aiogram.types import FSInputFile

#import from library my project
from Bot.config.create_bot import bot 
from Bot.config.config import LOG_CHANNEL_ID

#import from library python 
from datetime import datetime
import logging


current_datetime = datetime.now() # your timezone time
datetime_formatted = current_datetime.strftime("%Y-%m-%d  %H:%M:%S") # Format the current time as "hour:min:sec"

def logger_name():
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler=logging.FileHandler(filename='warning.log',encoding='utf-8',mode='w')
    formatter=logging.Formatter("%(levelname)s %(asctime)s : %(message)s (Line: %(lineno)d)")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


async def send_loggingFile():
    warning= await bot.send_document(chat_id=LOG_CHANNEL_ID,document=FSInputFile(path='warning.log',filename =f'WARNING {datetime_formatted}.log'))
    debug=await bot.send_document(chat_id=LOG_CHANNEL_ID,document=FSInputFile(path='info.log',filename=f"INFO{datetime_formatted}.log"))
    return warning ,debug

async def logging_info(user_id,text,handler):
    logging.info(msg=f"client: {user_id}, message: {text}, handler: {handler},time: {datetime_formatted}")
        