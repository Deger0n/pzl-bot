import keyboard
from create_bot import bot
from data_base.db_handler import db_work
from general_lists import set_state_list, work_list, text_list


async def work_ask(callback):
    index = work_list.index(callback.data)
    await set_state_list[index].set()
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=keyboard.close)
    await bot.send_message(callback.from_user.id, text_list[index])
    if index <= 1: await db_work.sql_work_send_without_html(callback.from_user.id, callback)


async def work_load(state, user, message):
    if message.text in keyboard.buttons:
        await message.answer("Вы не можете использовать функции меню, пока вы не завершите изменение текста, или не отмените действие")
        await work_load()
    await db_work.sql_work_set(user, message.text, state)
    await db_work.sql_work_send(user, message.text, state)
    await state.finish()