import sqlite3 as sq
from create_bot import bot
import keyboard


def sql_start_balance():
    global base, cur
    base = sq.connect('data_base/pzl.db')
    cur = base.cursor()


async def sql_balance_set(balance_add, user):
    balance = cur.execute('SELECT balance FROM game WHERE user == ?', (user,)).fetchone()[0]
    new_balance = balance + balance_add
    cur.execute('UPDATE game SET balance == ? WHERE user == ?', (new_balance, user))
    base.commit()


async def sql_balance_get(user):
    return cur.execute('SELECT balance FROM game WHERE user == ?', (user,)).fetchone()[0]


async def sql_balance_send(user):
    await bot.send_message(user,
                           'Счёт: ' + str(cur.execute('SELECT balance FROM game WHERE user == ?', (user,)).fetchone()[0]),
                           reply_markup=keyboard.history_return)