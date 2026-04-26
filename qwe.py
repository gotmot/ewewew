import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

products_data = [
    ('Laptop', 1200.50, 5),
    ('Phone', 800.00, 10),
    ('Tablet', 300.00, 0)
]
cursor.executemany('INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)', products_data)

cursor.execute('UPDATE Products SET quantity = 10 WHERE name = ?', ('Laptop',))

cursor.execute('DELETE FROM Products WHERE quantity = 0')

connection.commit()

cursor.execute('SELECT id, name, price, quantity FROM Products')
result = cursor.fetchall()

print(result)

connection.close()
