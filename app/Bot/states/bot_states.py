from aiogram.fsm.state import State,StatesGroup

class ProductInfo(StatesGroup):
    request=State()
    