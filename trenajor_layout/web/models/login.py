import sqlite3

def login_user(username, password):
    print(username)
    print(password)
    try:
        url = r"C:\work\LDPK\trenajor_layout\trenajor_layout\web\db\storage.db"
        connect = sqlite3.connect(url)
        #connect = sqlite3.connect("../db/storage.db")
        cursor = connect.cursor()
        cursor.execute(
            "SELECT Password FROM users WHERE User =?"
        )
        get_password = cursor.fetchone()
        if password == get_password[0]:
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
    
def login_session():
    try:
        connect = sqlite3.connect("../db/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT User FROM user_session WHERE id =?", (1,))
        get_user_online = cursor.fetchone()
        user_online = []
        for name in get_user_online:
            user_online.append(name)
        connect.close()
        return user_online[0]
    except Exception as error:
        user_online = "ERROR"
        print(error)
        return user_online