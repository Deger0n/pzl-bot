import datetime
import re
import sqlite3 as sq

from aiogram.utils.exceptions import CantParseEntities
from create_bot import bot, MAX_LEN
import keyboard


def sql_start_history():
    global base, cur
    base = sq.connect('data_base/pzl.db')
    cur = base.cursor()


async def sql_history_send(user, callback):
    history = cur.execute('SELECT history FROM game WHERE user == ?', (user,)).fetchone()[0]
    try:
        for i in range(0, len(history), MAX_LEN):
            await bot.send_message(callback.from_user.id, "<b>История счёта:</b>" +
                           history[i:i+MAX_LEN],
                                   reply_markup=keyboard.history_delete)


    except CantParseEntities:
        await bot.send_message(callback.from_user.id, '<b>Вы сломали разметку HTML</b>\n',
                               reply_markup=keyboard.history_replace_html)



async def sql_history_replace_html(user, callback):
    history = cur.execute('SELECT history FROM game WHERE user == ?', (user,)).fetchone()[0]
    history = re.sub(r"<[^>]*>", "", history)
    cur.execute('UPDATE game SET history == ? WHERE user == ?', (history, user))
    base.commit()
    await bot.send_message(callback.from_user.id, "<b>HTML успешно вырезан!</b>")
    await bot.send_message(callback.from_user.id, "Вы вновь можете посмотреть свою историю!", reply_markup=keyboard.history_return)



async def sql_history_set(text, user):
    history = cur.execute('SELECT history FROM game WHERE user == ?', (user,)).fetchone()[0]
    time_zone = cur.execute('SELECT time_zone FROM game WHERE user == ?', (user,)).fetchone()[0]
    default_tz = 3600 * 3

    money_now = re.findall(r"\d+", text)[0]
    sign_now = re.findall(r"[+-]", text)[0]
    text_now = re.findall(r"[\s\S]+", text)[0].replace(money_now, "")[1:]
    if text_now != "" and text_now[0] != " ":
        text_now = " " + text_now

    history_new = str(history) + "\n<b>" + sign_now + money_now + "</b>" + text_now +"  —  "+\
                    datetime.datetime.fromtimestamp(int(datetime.datetime.now().timestamp()) + time_zone + default_tz).\
                        strftime("%H:%M %d.%m.%y")
    cur.execute('UPDATE game SET history == ? WHERE user == ?', (history_new, user))
    base.commit()


async def sql_history_delete(user, callback):
    cur.execute('UPDATE game SET history == ? WHERE user == ?', (' ', user))
    base.commit()
    await bot.send_message(callback.from_user.id, 'История была очищена')