from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from create_bot import dp
from create_bot import FSMgame
from function.work import work_edit
from data_base.db_handler import db_work
import keyboard


async def work_send(message: types.Message):
    await db_work.sql_work_send(message.from_user.id, message.text, None)

async def work_inline(callback: types.CallbackQuery):
    await work_edit.work_ask(callback)

async def work_load(message: types.Message, state: FSMContext):
    await work_edit.work_load(state, message.from_user.id, message)


def register_handlers_work(dp: Dispatcher):
    dp.register_message_handler(work_send, text=[keyboard.buttons[2], keyboard.buttons[3]], state=None)
    dp.register_callback_query_handler(work_inline, text=['receive_edit', 'spend_edit', 'receive_add', 'spend_add'])
    dp.register_message_handler(work_load, content_types=['text'], state=[FSMgame.receive_edit_state, FSMgame.spend_edit_state,
                                                                    FSMgame.receive_add_state, FSMgame.spend_add_state])
register_handlers_work(dp)
