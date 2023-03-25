from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from create_bot import dp
from data_base import data_base_start
import keyboard



async def welcome(message: types.Message):
    await message.answer('<b>Привет, прочти руководство, после чего присутпай к использованию бота:</b>\n'
                         'https://telegra.ph/CHto-takoe-pzl-bot-08-23',
                         reply_markup=keyboard.keyboard)
    await data_base_start.add_user(message.from_user.id)



async def close(callback: types.CallbackQuery, state: FSMContext):
    state_get = await state.get_state()
    if 'receive' in state_get:
        await callback.message.edit_reply_markup(reply_markup=keyboard.receive)
    elif 'spend' in state_get:
        await callback.message.edit_reply_markup(reply_markup=keyboard.spend)
    elif 'operation' in state_get:
        await callback.message.edit_reply_markup(reply_markup=None)

    await state.finish()
    await callback.answer()
    await callback.message.answer('Действие отменено', reply_markup=keyboard.keyboard)



def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['start', 'help'])
    dp.register_callback_query_handler(close, text='close', state="*")
register_handlers_start(dp)
