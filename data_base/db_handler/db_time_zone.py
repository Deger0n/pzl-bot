import sqlite3 as sq
from create_bot import bot, FSMgame
import keyboard

def sql_start_tz():
    global base, cur
    base = sq.connect('data_base/pzl.db')
    cur = base.cursor()


async def sql_time_zone_set(user, zone):
    cur.execute('UPDATE game SET time_zone == ? WHERE user == ?', (zone, user))
    base.commit()


async def sql_time_zone_send_and_ask(user):
    await FSMgame.time_zone_state.set()
    zone = int(cur.execute('SELECT time_zone FROM game WHERE user == ?', (user,)).fetchone()[0]/3600)
    if zone > 0: zone = "+" + str(zone)
    await bot.send_message(user, "Ваш часовой пояс на данный момент: <b>" + str(zone) + "</b>")
    await bot.send_message(user, 'Введите ваш часовой пояс относительно МСК\nПример: <b>+3</b>\n'
                                 'Если вы хотите поставить часововой пояс МСК, напишите <b>+0</b> или <b>-0</b>', reply_markup=keyboard.close)