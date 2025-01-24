from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from Bot.keyboards.client_kb import *
from Bot.logging.logging_bot import logger_name,send_loggingFile,logging_info
from Bot.functions.client_func import exists_user,create_user_record,create_product
from Bot.states.bot_states import *