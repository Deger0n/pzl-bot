from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ============================<МЕНЮ>============================
buttons = ['💰 Счёт', '📦 Операции', '📗 Заработок', '📘 Товары']
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(buttons[0], buttons[1]).add(buttons[2], buttons[3])


# ============================<ОТМЕНИТЬ>============================
close = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="Отменить", callback_data="close"))


# ============================<ЗАРАБОТАТЬ>============================
receive = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="Редактировать", callback_data="receive_edit")).\
    add(InlineKeyboardButton(text="Добавить", callback_data="receive_add"))


# ============================<ТОВАРЫ>============================
spend = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="Редактировать", callback_data="spend_edit")).\
    add(InlineKeyboardButton(text="Добавить", callback_data="spend_add"))


# ============================<ИСТОРИЯ>============================
history_return = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="История", callback_data="history_return"))
history_delete = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="Очистить историю", callback_data="history_delete"))

history_replace_html = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text="Очистить историю", callback_data="history_delete")).\
    add(InlineKeyboardButton(text="Вырезать HTML", callback_data="history_replace_html"))