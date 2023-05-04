from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


def generate_admin_menu():
    """
    Admin menu keyboard layout
    :return: markup
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(
        KeyboardButton(text="📃 Kurslar"),
        KeyboardButton(text="📣 E'lon berish"),
    )
    markup.row(
        KeyboardButton(text="📄 Statistika"),
        KeyboardButton(text="🖥️ Ochiq darslar")
    )
    return markup
