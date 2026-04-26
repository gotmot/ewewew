import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL
)
''')

orders_data = [
    (1, 'Алексей', '2023-10-01', 1500.0),
    (2, 'Мария', '2023-10-02', 2300.0),
    (3, 'Алексей', '2023-10-03', 800.0),
    (4, 'Иван', '2023-10-04', 1200.0),
    (5, 'Мария', '2023-10-05', 3000.0),
    (6, 'Елена', '2023-10-06', 450.0)
]

cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?, ?)', orders_data)
connection.commit()

print("1. Количество заказов каждого клиента:")
query1 = '''
SELECT customer_name, COUNT(*) as order_count
FROM Orders
GROUP BY customer_name;
'''
cursor.execute(query1)
for row in cursor.fetchall():
    print(f"Клиент: {row[0]}, Заказов: {row[1]}")

print("\n2. Клиенты, сделавшие более одного заказа:")
query2 = '''
SELECT customer_name, COUNT(*) as order_count
FROM Orders
GROUP BY customer_name
HAVING COUNT(*) > 1;
'''
cursor.execute(query2)
for row in cursor.fetchall():
    print(f"Клиент: {row[0]}, Заказов: {row[1]}")

connection.close()
