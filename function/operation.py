from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from create_bot import dp, FSMgame
from data_base.db_handler import db_operation, db_history
import keyboard
import re


async def operation_send(message: types.Message):
    await message.answer('Введите операцию', reply_markup=keyboard.close)
    await FSMgame.operation_state.set()


async def operation_load(message: types.Message, state: FSMContext):
    number_list = re.findall(r"\d+", message.text)
    if message.text in keyboard.buttons:
        await message.answer("Вы не можете использовать функции меню, пока вы не введёте операцию, или не отмените её")
        await operation_load()

    elif len(number_list) == 0 or message.text[0] != "+" and message.text[0] != "-":
        await message.answer('<b>Сообщение должно содержать цифры и начинаться с "+" или "-"</b>')
        await message.answer('Повторите ввод операции или отмените её')
        await operation_load()


    score = int(number_list[0])
    if message.text[0] == "-":
        if await db_operation.sql_balance_get(message.from_user.id) < score:
            await message.answer("У вас недостаточно средств!", reply_markup=keyboard.keyboard)
            await state.finish()
            return
        score = -score

    await db_operation.sql_balance_set(score, message.from_user.id)
    await db_history.sql_history_set(message.text, message.from_user.id)

    if score >= 0: await message.answer(str(score) + ' очков зачислено на баланс', reply_markup=keyboard.keyboard)
    else: await message.answer(str(-score) + ' очков списано с баланса', reply_markup=keyboard.keyboard)
    await state.finish()



def register_handlers_operation(dp: Dispatcher):
    dp.register_message_handler(operation_send, text=keyboard.buttons[1])
    dp.register_message_handler(operation_load, content_types=['text'], state=FSMgame.operation_state)
register_handlers_operation(dp)
