import pymysql


class Database:
    def __init__(self, db_name: str, db_password: str, db_user: str, db_host: str, db_port: int) -> None:
        """
        :returns
        :param db_name:
        :param db_password:
        :param db_user:
        :param db_host:
        :param db_port:
        """
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_host = db_host
        self.db_port = db_port

    @property
    def db(self) -> pymysql.Connection:
        """
        :return: database connection
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
        :param sql:
        :param params:
        :param commit:
        :param fetchall:
        :param fetchone:
        :return: tuple if there is returning some data from a database or None if there is just committing something
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

