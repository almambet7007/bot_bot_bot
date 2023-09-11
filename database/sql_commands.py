import sqlite3
from database import sql_query

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def create_database(self):
        if self.connection:
            print("Database connected successfully:)")

        self.connection.execute(sql_query.create_user_table_query)
        self.connection.execute(sql_query.create_table_for_answer)
        self.connection.execute(sql_query.create_table_for_ban)
        self.connection.commit()

    def sql_insert_user_query(self,telegram_id,username , first_name, last_name):
        self.cursor.execute(sql_query.insert_user_query,(None,
                                                        telegram_id,
                                                        username,
                                                        first_name,
                                                        last_name))
        self.connection.commit()

    def sql_select_users(self):
        self.cursor.row_factory = lambda  cursor, row: {'username': row[0]}
        return self.cursor.execute(sql_query.select_users_query).fetchall()

    def sql_insert_answer_query(self,id_user,username,first_name, quiz, quiz_option):
        self.cursor.execute(sql_query.insert_answer_table_query,(id_user,
                                                                 username,
                                                                 first_name,
                                                                 quiz,
                                                                 quiz_option))
        self.connection.commit()

    def sql_insert_ban_table(self,id_user, username, id_group):
        self.cursor.execute(sql_query.insert_ban_table,(id_user,
                                                        username,
                                                        id_group
                                                        ))
        self.connection.commit()

    def sql_select_ban_table(self,id_user,username, id_group):
        return self.cursor.execute(sql_query.select_ban_table,([id_user,username,id_group])).fetchall()