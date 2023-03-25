from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='TOKEN', parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
MAX_LEN = 4000

class FSMgame(StatesGroup):
    receive_edit_state = State()
    receive_add_state = State()
    spend_edit_state = State()
    spend_add_state = State()
    operation_state = State()
    time_zone_state = State()