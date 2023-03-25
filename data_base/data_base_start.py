import sqlite3 as sq


def sql_start_game():
    global base, cur
    base = sq.connect('data_base/pzl.db')
    cur = base.cursor()
    if base:
        print('база данных онлайн')
    base.execute('CREATE TABLE IF NOT EXISTS game(user INTEGER PRIMARY KEY, receive TEXT, spend TEXT, balance INTEGER, history TEXT, time_zone INTEGER)')
    base.commit()


async def add_user(user):
    if cur.execute(f'SELECT user FROM game WHERE user == ?', (user,)).fetchone() is None:
        cur.execute('INSERT INTO game VALUES (?, ?, ?, ?, ?, ?)', (user, 'Пока что пусто', 'Пока что пусто', 0, ' ', 0))
        base.commit()



