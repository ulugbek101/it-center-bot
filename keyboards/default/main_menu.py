from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(
        KeyboardButton(text="📃 Kurslar haqida"),
        KeyboardButton(text="🖋️ Ochiq darsga yozilish"),
    )
    markup.row(
        KeyboardButton(text="📞 Bog'lanish"),
        KeyboardButton(text="📌 Joylashuv", request_location=True),
    )
    markup.row(
        KeyboardButton(text="⚙️ Sozlamalar"),
        KeyboardButton(text="📝 Fikr qoldirish"),
    )

    return markup

