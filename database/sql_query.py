create_user_table_query = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (id INTEGER PRIMARY KEY,
        telegram_id INTEGER,
        username CHAR(50),
        first_name CHAR(50),
        last_name CHAR(50),
        UNIQUE (telegram_id))
"""
insert_user_query = """ INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?)"""

select_users_query = """SELECT username FROM telegram_users"""

create_table_for_answer = """
    CREATE TABLE IF NOT EXISTS answer_table
    (id INTEGER PRIMARY KEY,
    id_user CHAR(50),
    username CHAR(50),
    firstname CHAR(50),
    quiz CHAR(50),
    quiz_option INTEGER,
    FOREIGN KEY (id_user) REFERENCES telegram_users (id))
    """

insert_answer_table_query = """INSERT INTO answer_table(id_user,username,firstname, quiz,quiz_option) VALUES (?,?,?,?,?)"""


create_table_for_ban = """
    CREATE TABLE IF NOT EXISTS ban_table
    (id INTEGER PRIMARY KEY,
    id_user CHAR(50),
    username CHAR(50),
    id_group INTEGER,
    FOREIGN KEY (id_user) REFERENCES telegram_users (id)
    )"""

insert_ban_table = """INSERT INTO ban_table(id_user, username, id_group ) VALUES(?,?,?) """

select_ban_table = """SELECT id_user FROM ban_table WHERE id_user = ?  AND username = ? AND id_group = ?"""