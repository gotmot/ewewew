import sqlite3

conn = sqlite3.connect('BookStore.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    AuthorID INTEGER,
    Price REAL,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
)''')

cursor.execute("INSERT INTO Authors (FirstName, LastName) VALUES ('Лев', 'Толстой')")
cursor.execute("INSERT INTO Books (Title, AuthorID, Price) VALUES ('Война и мир', 1, 850.50)")
conn.commit()
print("Данные успешно добавлены.")

cursor.execute("DELETE FROM Books")
cursor.execute("DELETE FROM Authors")
conn.commit()
print("Данные удалены (команда DELETE выполнена).")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(f"Таблицы, оставшиеся в базе: {[table[0] for table in tables]}")

conn.close()
