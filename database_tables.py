from loader import db


def create_users_table() -> None:
    """
    Create Users table in database
    :return: None
    """
    sql = """
        CREATE TABLE IF NOT EXISTS Users(
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            chat_id BIGINT NOT NULL UNIQUE,
            username VARCHAR(255),
            fullname VARCHAR(255)
        );
    """
    db.execute(sql, commit=True)


def create_courses_table() -> None:
    """
    Create Courses table in a database
    :return: None
    """
    sql = """
         CREATE TABLE IF NOT EXISTS Courses(
            course_id INT PRIMARY KEY AUTO_INCREMENT,
            course_name VARCHAR(255) NOT NULL UNIQUE,
            course_desc_path VARCHAR(255),
            course_image_path VARCHAR(255)
        );
    """
    db.execute(sql, commit=True)


# create_users_table()
# create_courses_table()

