from tools.keyboard_generators import generate_reply_keyboard


def generate_courses_management_menu():
    """
    Generate course management keyboard menu
    :return: markup
    """
    menu = {
        "🖋 Yangi kurs qo'shish️": "text",
        "🗑️ Kursni o'chrish": "text",
        "👈 Bosh menu": "text",
    }

    markup = generate_reply_keyboard(
        menu=menu,
        in_row=2
    )

    return markup
