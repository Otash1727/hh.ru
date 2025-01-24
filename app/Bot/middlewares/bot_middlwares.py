from typing import Callable,Awaitable,Dict,Any
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject,Message,CallbackQuery
from datetime import timedelta,datetime
from Bot.functions.client_func import exists_user



class AntiFloodMiddleware(BaseMiddleware):
    # Dictionary to store the last interaction time of each user
    # Keys are user IDs (int), and values are datetime objects
    time_updates: dict[int, datetime] = {}

    # Time interval to limit the rate of messages from a single user
    # Users can only interact once within this time period
    timedelta_limiter: timedelta = timedelta(seconds=1)  # Set the desired time limit

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],  # The function to handle events
        event: TelegramObject,  # The incoming Telegram update (e.g., a message or callback query)
        data: Dict[str, Any],  # Additional data/context for handling the event
    ) -> Any:
        # Check if the incoming event is either a Message or CallbackQuery
        if isinstance(event, (Message, CallbackQuery)):
            # Extract the user's unique ID from the event
            user_id1 = event.from_user.id

            # Check if the user ID already exists in the time_updates dictionary
            if user_id1 in self.time_updates.keys():
                # Check if the current time exceeds the allowed interval since the last interaction
                if (datetime.now() - self.time_updates[user_id1]) > self.timedelta_limiter:
                    # Update the last interaction time for the user
                    self.time_updates[user_id1] = datetime.now()
                    # Proceed with the event handling
                    return await handler(event, data)
            else:
                # If the user ID is not in the dictionary, this is their first interaction
                # Record the current time as the last interaction time for this user
                self.time_updates[user_id1] = datetime.now()
                # Proceed with the event handling
                return await handler(event, data)


class UserExistsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],  # The function to handle events
        event: TelegramObject,  # The incoming Telegram update (e.g., a message or callback query)
        data: Dict[str, Any],  # Additional data/context for handling the event
    ) -> Any:
        # Check if the incoming event is a Message or CallbackQuery
        if isinstance(event, (Message, CallbackQuery)):
            # Extract the user ID from the event
            user_id = event.from_user.id

            # Check if the user exists in the database or other storage
            is_user = await exists_user(user_id=user_id)

            if not is_user:
                # If the user doesn't exist, mark them as a new user
                is_user: bool = False
                # Add the user status to the data dictionary
                data['is_user'] = is_user
                # Pass the event to the handler for further processing
                return await handler(event, data)

            else:
                # If the user exists, mark them as not a new user
                is_user: bool
                data['is_user'] = True
                # Pass the event to the handler for further processing
                return await handler(event, data)
