from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def generate_reply_keyboard(menu: dict, in_row: int = 2, markup: ReplyKeyboardMarkup = None):
    """
    Reply keyboard generator
    :param menu:
    :param in_row:
    :param markup:
    :return: markup
    """
    if markup is None:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    in_row = in_row
    start = 0
    end = in_row

    rows = len(menu) // 2
    if rows % 2 != 0:
        rows += 1

    for _ in range(rows):
        row = []
        for btn_text, btn_type in list(menu.items())[start:end]:
            btn = None
            if btn_type == "location":
                btn = KeyboardButton(
                    text=btn_text,
                    request_location=True,
                )
            elif btn_type == "contact":
                btn = KeyboardButton(
                    text=btn_text,
                    request_contact=True,
                )
            else:
                btn = KeyboardButton(
                    text=btn_text,
                )
            row.append(btn)
        markup.row(*row)
        start = end
        end += in_row
    return markup
