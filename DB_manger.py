import mysql.connector
from mysql.connector import MySQLConnection

import config as cfs


class dbConnector:
    def __init__(self):
        self.mydb: MySQLConnection = None

    def __del__(self):
        print("INFO  Closing connection")
        self.mydb.close()

    def open_connection(self):
        self.mydb = mysql.connector.connect(
            host=cfs.host,
            user=cfs.user,
            password=cfs.password,
            database=cfs.database
        )

    def get_all_objects(self, table_name: str) -> list:
        """
        This function return all objects from current table. DEBUG FUNCTION\n
        :param table_name: necessary table name
        :return: list ob objects
        """
        print(f"INFO  Get all objects from table: {table_name}")

        if not self.mydb:
            print(f"INFO  Conn ong is empty. Opening new connection...")
            self.open_connection()

        mycursor = self.mydb.cursor()

        mycursor.execute(f"SELECT * FROM {table_name}")

        myresult = mycursor.fetchall()

        res = []
        for x in myresult:
            res.append(x)
        print(f"INFO  Got items: {len(res)}")
        return res

    def get_user_by_username(self, username: str):
        print(f"INFO  Get user: {username}")

        if not self.mydb:
            print(f"INFO  Conn ong is empty. Opening new connection...")
            self.open_connection()

        mycursor = self.mydb.cursor()

        sql = f"SELECT * FROM users WHERE username ='{username}'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        res = []
        for x in myresult:
            res.append({
                "id": x[0],
                "username": x[1],
                "password": x[2],
                "last_login": x[3],
                "token": x[4]
            })
        if len(res) == 0:
            print(f"INFO  There is no accounts with current username: {username}")
            return {}
        print(f"INFO  Got items: {len(res)}")
        return res[0]  # TODO: need to set up user as unic param in DB
