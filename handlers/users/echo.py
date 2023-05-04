from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    """
    Send the same message that was accepted,
    if message was not handled by any handler
    :param message:
    :return:
    """
    await message.answer(message.text)
