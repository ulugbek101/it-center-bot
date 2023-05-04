from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.state_cancel_btn import generate_state_cancel_btn
from keyboards.admin.default.management import generate_courses_management_menu
from filters.is_admin import IsAdmin
from loader import dp, db
from states.courses.course_add import CourseAddForm


@dp.message_handler(IsAdmin(), Text(equals="🖋 Yangi kurs qo'shish️"))
async def request_course_name(message: Message, state: FSMContext):
    """
    Start adding a course, request course name
    :param message:
    :param state:
    :return:
    """
    await message.answer(
        text="Kursga nom bering:  \
             \n- Berilgan nom avvalgi kurslar nomiga o'xshamasin \
             \n- Ma'noli nom bo'lsin (Python, JavaScript, Kompyuter savodxonligi)",
        reply_markup=generate_state_cancel_btn(),
    )
    await CourseAddForm.course_name.set()


@dp.message_handler(state=CourseAddForm.course_name)
async def save_course_name_and_request_course_description(message: Message, state: FSMContext):
    """
    Save course name from previous state and request course description
    :param message:
    :param state:
    :return:
    """
    await state.update_data(course_name=message.text)
    await message.answer(
        text="Kursga ta'rif bering (Yo'nalish haqida, afzalliklari, narxi, davomiyligi, ...)",
        reply_markup=generate_state_cancel_btn(),
    )
    await CourseAddForm.course_description.set()


@dp.message_handler(state=CourseAddForm.course_description)
async def save_course_description_and_request_course_image(message: Message, state: FSMContext):
    """
    Save course description from previus state and request course image
    :param message:
    :param state:
    :return:
    """
    await state.update_data(course_description=message.text)
    await message.answer(
        text="Kurs uchun \".jpg\" formatda rasm yuboring",
        reply_markup=generate_state_cancel_btn(),
    )
    await CourseAddForm.course_image.set()


@dp.message_handler(state=CourseAddForm.course_image, content_types="photo")
async def save_course_image_and_finish_state(message: Message, state: FSMContext):
    """
    Save course information in database if its valid,
    sends a warning message otherwise
    :param message:
    :param state:
    :return:
    """
    data = await state.get_data()

    special_symbols = ["/", "\\", " ", "-", ":", ";", "?", "!"]
    course_name = data.get("course_name")
    course_description = data.get("course_description")

    """
    Validating course and replacing all unnecessary symbols
    """
    for symbol in special_symbols:
        course_name = course_name.replace(symbol, "_")

    course_photo_destination = f"assets/courses/images/{course_name}.jpg"
    course_description_destination = f"assets/courses/descriptions/{course_name}.txt"

    """
    Saving course photo
    """
    await message.photo[-1].download(destination_file=course_photo_destination)

    """
    Saving course description to ".txt" file
    """
    with open(file=course_description_destination, mode="w") as file:
        file.write(course_description)

    try:
        db.add_course(
            course_name=course_name,
            course_description_path=course_description_destination,
            course_image_path=f"{course_name}.jpg",
        )
        await message.answer(
            text="✅ Kurs muvaffaqiyatli qo'shildi",
            reply_markup=generate_courses_management_menu(),
        )
    except:
        await message.answer(
            text="🤔 Nimadir noto'g'ri ketdi",
            reply_markup=generate_courses_management_menu(),
        )

    await state.finish()
