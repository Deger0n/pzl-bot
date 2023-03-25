from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp
from data_base.db_handler import db_operation, db_history
import keyboard


async def balance_send(message: types.Message):
    await db_operation.sql_balance_send(message.from_user.id)


async def history_send(callback: types.CallbackQuery):
    await db_history.sql_history_send(callback.from_user.id, callback)
    await callback.answer()


async def history_delete(callback: types.CallbackQuery):
    await db_history.sql_history_delete(callback.from_user.id, callback)
    await callback.answer()


async def history_replace_html(callback: types.CallbackQuery):
    await db_history.sql_history_replace_html(callback.from_user.id, callback)
    await callback.answer()


def register_handlers_balance(dp: Dispatcher):
    dp.register_message_handler(balance_send, text=keyboard.buttons[0])
    dp.register_callback_query_handler(history_delete, text='history_delete')
    dp.register_callback_query_handler(history_send, text='history_return')
    dp.register_callback_query_handler(history_replace_html, text='history_replace_html')
register_handlers_balance(dp)
