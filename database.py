import sqlite3

class DatabaseManager:

    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.__con = sqlite3.connect(self.db_name)
        self.__cur = self.__con.cursor()

    def create_tables(self):
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER UNIQUE,
            name VARCHAR(50) NOT NULL,
            phone_number VARCHAR UNIQUE
           
        )""")
        
    def add_user(self, data: dict):
        try:
            self.__cur.execute(f"INSERT INTO users(chat_id, name, phone_number) VALUES(?,?,?)",
                               (data.get("chat_id"), data.get("name"), data.get("phone_number")))
            self.__con.commit()
        except Exception as ex:
            print(ex)
            return False
    
    def get_user_by_id(self, chat_id: int):
        try:
            user = self.__cur.execute(f"SELECT * FROM users WHERE chat_id=?", (chat_id, )).fetchone()
            return user
        except Exception as ex:
            print(ex)
            return False