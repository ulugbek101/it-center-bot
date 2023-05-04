from aiogram.types import Message

from loader import dp
from keyboards.admin.default.admin_panel import generate_admin_menu
from filters.is_admin import IsAdmin


@dp.message_handler(IsAdmin(), commands="admin")
async def admin_menu(message: Message):
    await message.answer(
        text="✅ Admin panelga o'tdingiz",
        reply_markup=generate_admin_menu(),
    )
