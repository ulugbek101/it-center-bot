from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.default.state_cancel_btn import generate_state_cancel_btn
from keyboards.inline.courses_inline_menu import generate_courses_inline_menu
from keyboards.admin.default.management import generate_courses_management_menu
from filters.is_admin import IsAdmin
from loader import dp, db


@dp.message_handler(IsAdmin(), Text(equals="🗑️ Kursni o'chrish"))
async def show_course_menu_to_remove(message: Message):
    """
    Displays courses inline menu to remove one of them
    :param message:
    :return:
    """
    courses = db.get_courses()

    if len(courses) == 0:
        await message.answer(
            text="🤔 Kurslar ro'yxati bo'sh"
        )
    else:
        await message.answer(
            text="O'chirilishi kerak bo'lgan kursni tanlab, ustiga bosing",
            reply_markup=generate_state_cancel_btn(),
        )
        await message.answer(
            text="O'chirish mumkin bo'lgan kurslar ro'yxati",
            reply_markup=generate_courses_inline_menu(
                prefix="delete-course",
                menu=courses,
            )
        )


@dp.callback_query_handler(lambda call: "delete-course" == call.data.split(":")[0])
async def remove_course(call: CallbackQuery):
    """
    Deletes course that was selected and rerenders keyboard buttons
    :param call:
    :return:
    """
    course_id = int(call.data.split(":")[-1])
    courses = db.get_courses()

    await call.message.delete()
    await call.message.answer(
        text="Kurs o'chirildi ✅",
        reply_markup=generate_courses_management_menu()
    )
    db.remove_course(course_id=course_id)
