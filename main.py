from aiogram.utils import executor
from create_bot import dp
from data_base import data_base_start
from data_base.db_handler import db_operation, db_history, db_work, db_time_zone
from function import start, history_handler, operation, time_zone
from function.work import work_handler


async def on_startup(_):
    print('бот онлайн')
    data_base_start.sql_start_game()
    db_history.sql_start_history()
    db_operation.sql_start_balance()
    db_work.sql_start_work()
    db_time_zone.sql_start_tz()


start.register_handlers_start(dp)
history_handler.register_handlers_balance(dp)
operation.register_handlers_operation(dp)
work_handler.register_handlers_work(dp)
time_zone.register_handlers_tz(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
