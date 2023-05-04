from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from loader import dp, db
from keyboards.admin.default.admin_panel import generate_admin_menu
from keyboards.admin.default.management import generate_courses_management_menu
from filters.is_admin import IsAdmin


@dp.message_handler(IsAdmin(), commands="admin")
async def admin_menu(message: Message):
    """
    Display admin menu if user is an admin
    :param message:
    :return:
    """
    await message.answer(
        text="✅ Admin panelga o'tdingiz",
        reply_markup=generate_admin_menu(),
    )


@dp.message_handler(IsAdmin(), Text(equals="📃 Kurslar"))
async def display_course_management_menu(message: Message):
    """
    Display course management menu for admin user
    :param message:
    :return:
    """
    courses = db.get_courses()

    if len(courses) == 0:
        text = "🤔 Kurslar ro'yxati bo'sh"
    else:
        text = f"Hozirda {len(courses)} ta kurs ro'yxatga olingan:\n"
        for count, course in enumerate(courses, start=1):
            text += f"\n{count}. {course[1].capitalize().replace('_', ' ')}"

    await message.answer(
        text=text,
        reply_markup=generate_courses_management_menu(),
    )
