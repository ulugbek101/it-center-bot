from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_state_cancel_btn(markup: ReplyKeyboardMarkup = None):
    """
    Cancel any state
    :param markup:
    :return: markup: ReplyKeyboardMarkup
    """
    if not markup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    markup.row(
        KeyboardButton(text="❌ Bekor qilish"),
    )

    return markup
