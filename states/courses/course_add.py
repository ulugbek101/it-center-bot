from aiogram.dispatcher.filters.state import State, StatesGroup


class CourseAddForm(StatesGroup):
    course_name = State()
    course_description = State()
    course_image = State()
