from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.main_menu import generate_main_menu

from filters.is_private import IsPrivate
from loader import db


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    """
    Display main menu keyboard for users and send greeting text
    :param message:
    :return:
    """
    text = f" \
    Assalomu alaykum <b>{message.from_user.full_name}</b> 👋 \
    \n\nIT Center Bag'dod rasmiy botiga xush kelibsiz ! \
    \nBu yerda markazimiz hamda kurslarimiz haqida to'lliq ma'lumot olishingiz mumkin 😊 \
    "
    with open(file="assets/bot/logo/it-center.jpeg", mode="rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption=text,
            parse_mode="HTML",
            reply_markup=generate_main_menu(),
        )

    try:
        """
        Trying to register user in a database after we answer a user, 
        if a chat_id fields unique constraint's error occurs, then we just pass it
        """
        db.register_user(
            chat_id=message.from_user.id,
            username=message.from_user.username,
            fullname=message.from_user.full_name,
        )
    except:
        pass
