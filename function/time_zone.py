from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext

import keyboard
from create_bot import dp, FSMgame
from data_base.db_handler import db_time_zone
import re


async def time_zone_send(message: types.Message):
    await db_time_zone.sql_time_zone_send_and_ask(message.from_user.id)


async def time_zone_load(message: types.Message, state: FSMContext):
    number_list = re.findall(r"\d+", message.text)
    if len(number_list) == 0 or message.text[0] != "+" and message.text[0] != "-":
        await message.answer('<b>Сообщение должно содержать цифры и начинаться с "+" или "-"</b>')
        await message.answer('Если вы действительно хотите изменить часовой пояс - напишите команду ещё раз')
        return

    zone = int(number_list[0]) * 3600
    if message.text[0] == "-": zone = -zone
    await db_time_zone.sql_time_zone_set(message.from_user.id, zone)
    await message.answer("Часовой пояс успешно изменён!\n"
                         "Теперь ваша история будет записываться в новом часовом поясе.", reply_markup=keyboard.keyboard)
    await state.finish()


def register_handlers_tz(dp: Dispatcher):
    dp.register_message_handler(time_zone_send, commands=['time_zone', 'tz'])
    dp.register_message_handler(time_zone_load, content_types=['text'], state=FSMgame.time_zone_state)
register_handlers_tz(dp)