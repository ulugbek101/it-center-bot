from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.main_menu import generate_main_menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
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
