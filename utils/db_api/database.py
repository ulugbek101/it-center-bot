import pymysql


class Database:
    def __init__(self, db_name: str, db_password: str, db_user: str, db_host: str, db_port: int) -> None:
        """
        Initializing database credentials
        :param db_name:
        :param db_password:
        :param db_user:
        :param db_host:
        :param db_port:
        :returns
        """
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_host = db_host
        self.db_port = db_port

    @property
    def db(self) -> pymysql.Connection:
        """
        Returns database connection
        :return:
        """
        return pymysql.connect(
            database=self.db_name,
            password=self.db_password,
            user=self.db_user,
            host=self.db_host,
            port=self.db_port,
        )

    def execute(self, sql: str, params: tuple = None, commit: bool = False, fetchall: bool = False,
                fetchone: bool = False) -> tuple | None:
        """
        Returns Tuple if there is returning some data from a database or None if there is just committing something
        :param sql:
        :param params:
        :param commit:
        :param fetchall:
        :param fetchone:
        :return:
        """
        if not params:
            params = ()

        db = self.db
        cursor = db.cursor()
        cursor.execute(sql, params)
        data = None

        if commit:
            db.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        db.close()

        return data

    def register_user(self, chat_id: int, username: str, fullname: str) -> None:
        """
        Registers user in a database
        :param chat_id:
        :param username:
        :param fullname:
        :return:
        """
        sql = """
            INSERT INTO Users (chat_id, username, fullname) VALUES (%s, %s, %s);
        """
        self.execute(sql, (chat_id, username, fullname), commit=True)

    def add_course(self, course_name: str, course_description_path: str, course_image_path: str) -> None:
        """
        Add new course to a database
        :param course_name:
        :param course_description_path:
        :param course_image_path:
        :return:
        """
        sql = """
            INSERT INTO Courses (course_name, course_desc_path, course_image_path) VALUES (%s, %s, %s)
        """
        self.execute(sql, (course_name, course_description_path, course_image_path), commit=True)

    def remove_course(self, course_id: int):
        """
        Removes course by course id from database
        :param course_id:
        :return:
        """
        sql = """
            DELETE FROM Courses WHERE course_id = %s
        """
        self.execute(sql, (course_id,), commit=True)

    def get_courses(self):
        """
        Get all courses list
        :return:
        """
        sql = """
            SELECT * FROM Courses
        """
        return self.execute(sql, fetchall=True)
