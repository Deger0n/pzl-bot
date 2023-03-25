import sqlite3 as sq
from aiogram.utils.exceptions import CantParseEntities
from create_bot import bot, MAX_LEN
from general_lists import work_list, columns_list, keyboard_list
import keyboard


def sql_start_work():
    global base, cur
    base = sq.connect('data_base/pzl.db')
    cur = base.cursor()


async def sql_work_set(user, user_text, state):
    doing = str(await state.get_state()).replace('FSMgame:', '').replace('_state', '')
    column = doing.split("_")[0]
    index = work_list.index(doing)

    if index <= 1:
        cur.execute(f'UPDATE game SET {column} == ? WHERE user == ?', (user_text, user))

    else:
        old_text = cur.execute(f'SELECT {column} FROM game WHERE user == ?', (user,)).fetchone()[0] + "\n"
        cur.execute(f'UPDATE game SET {column} == ? WHERE user == ?', (old_text + user_text, user))
    base.commit()
    await bot.send_message(user, "Данные успешно обновлены", reply_markup=keyboard.keyboard)


async def sql_work_send(user, user_text, state):
    if state != None:
        index = columns_list.index( str(await state.get_state()).replace('FSMgame:', '').replace('_state', '').split("_")[0])

    else:
        index = keyboard.buttons.index(user_text) - 2


    text = cur.execute(f'SELECT {columns_list[index]} FROM game WHERE user == ?', (user,)).fetchone()[0]
    try:
        for i in range(0, len(text), MAX_LEN):
            await bot.send_message(user, f"<b>{keyboard.buttons[index + 2]}</b>\n" +
                                   text[i:i + MAX_LEN],
                                   reply_markup=keyboard_list[index])

    except CantParseEntities:
        await bot.send_message(user, f'<b>{keyboard.buttons[index + 2]}</b>\n'
                                     '<b>Вы сломали разметку HTML</b>\n'
                                     'Нажмите "Редактировать", возьмите свой текст, удалите лишние тэги, после чего '
                                     'отправьте боту новый текст, без лишних html тегов',
                               reply_markup=keyboard_list[index])



async def sql_work_send_without_html(user, callback):
    column = callback.data.split("_")[0]
    text = cur.execute(f'SELECT {column} FROM game WHERE user == ?', (user,)).fetchone()[0]
    for i in range(0, len(text), MAX_LEN):
        await bot.send_message(user, text[i:i + MAX_LEN], parse_mode="")
    await callback.answer()