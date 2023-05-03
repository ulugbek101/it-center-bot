from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp
from keyboards.default.main_menu import generate_main_menu


@dp.message_handler(Text(equals="❌ Bekor qilish"))
async def cancel_state(message: Message, state: FSMContext):
    """
    Function to cancel any state, and say that state is cancelled
    :param message:
    :param state:
    :return: message
    """
    if state is None:
        await message.answer(
            text="❎ Bekor qilindi",
            reply_markup=generate_main_menu(),
        )
        return None

    await state.finish()
    await message.answer(
        text="✅ Bekor qilindi",
        reply_markup=generate_main_menu(),
    )
