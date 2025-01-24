from aiogram import Router
from Bot.handlers import client,client_request
from Bot.config.create_bot import dp

router=Router()

dp.include_router(client.router)
dp.include_router(client_request.router)