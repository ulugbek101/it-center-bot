from tools.keyboard_generators import generate_inline_keyboard


def generate_courses_inline_menu(menu: tuple, prefix: str = "course-detail"):
    """
    Generates courses inline menu
    :param menu:
    :param prefix:
    :return:
    """
    markup = generate_inline_keyboard(prefix=prefix, menu=menu)
    return markup
