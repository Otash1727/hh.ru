from django.core.management.base import BaseCommand
from aiogram.methods import DeleteWebhook
from Bot.config.create_bot import bot,dp
from Bot.backup.backup_db import backup_postgresql_db
from Bot.middlewares.bot_middlwares import AntiFloodMiddleware,UserExistsMiddleware
from Bot.config.config import *
from aiogram.types import FSInputFile
import logging
import asyncio
from Bot import main

class Command(BaseCommand):
    help='Start The Telegram Bot'
    
    
    async def start_bot(self):
        try:
            # Configure logging
            logging.basicConfig(level=logging.INFO, encoding='utf-8', filemode='w', filename='info.log')
            
            # Set up middlewares
            dp.message.outer_middleware(middleware=AntiFloodMiddleware())
            dp.callback_query.outer_middleware(middleware=AntiFloodMiddleware())
            dp.message.middleware(UserExistsMiddleware())
            dp.callback_query.middleware(UserExistsMiddleware())

            # Include the main router
            dp.include_router(main.router)
            
            # Start the bot polling
            await bot(DeleteWebhook(drop_pending_updates=True))
            await dp.start_polling(bot)
        except Exception as e:
            print(f"Error starting bot: {e}")

    async def scheduled_task(self):
        try:
            print('Scheduled task started.')
            while True:
                logging.info("Scheduled task running...")  # Debug log
                await self.back_up_message()
                await asyncio.sleep(3600)  # Wait for 10 seconds
        except asyncio.CancelledError:
            logging.info("Scheduled task cancelled.")  # Debug log
           
        except Exception as e:
            logging.error(f"Error in scheduled task: {e}")  # Error log

    async def back_up_message(self):
        try:
            chat_id =BACK_UP_CHANNEL_ID # Replace with your target chat ID
            message_text = 'этот файл резервной копии базы данных'
            file = backup_postgresql_db(host =HOST,user =USER,password =PASSWORD,database_name =NAME)
            await bot.send_document(chat_id=chat_id, document=FSInputFile(path=file))
            await bot.send_message(chat_id=chat_id, text=message_text)
            logging.info("Hourly message sent successfully.")  # Debug log
        except Exception as e:
            logging.error(f"Error sending hourly message: {e}")  # Error log


    async def main(self):
        await asyncio.gather(
            self.start_bot(),
            self.scheduled_task()

        )
    
    def handle(self,*args, **kwargs):
        print('Bot online...')

        # Run the main function with asyncio.run()
        asyncio.run(self.main())