import sqlite3
from sqlite3 import Error

url = './db/data.db'

def check_table():
    connection = sqlite3.connect(url)
    cursor = connection.cursor()
    
    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    nickname TEXT
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def register_user(username, password):
    try:
        check_table()
        connection = sqlite3.connect(url)
        cursor = connection.cursor()
        cursor.execute(
        'INSERT INTO Users (username, password, nickname) VALUES (?, ?, ?)', 
        (f'{username}', f'{password}', '')
        )

        connection.commit()
        connection.close()
        msg = "SUCCES"
        return msg

    except Exception as Error:
        print(Error)
        msg = "FAIL"
        return msg



def login_user(username, password):
    try:
        #print(username)
        #print(password)
        check_table()
        connect = sqlite3.connect(url)
        cursor = connect.cursor()
        cursor.execute(
            'SELECT username, password FROM Users WHERE username == ?',
            (f'{username}',)
        )

        get_password = cursor.fetchone()
        #print(get_password)
        if password == get_password[1]:
            msg = "SUCCES"
            connect.close()
            return msg
        else:
            msg = "FAILED"
            connect.close()
            return msg

    except Exception as Error:
        print(Error)
        msg = "FAILED"
        return msg