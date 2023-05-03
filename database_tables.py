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


# create_users_table()
