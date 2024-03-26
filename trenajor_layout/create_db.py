import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    url = r"C:\work\LDPK\trenajor_layout\trenajor_layout\web\db\storage.db"
    create_connection(url)