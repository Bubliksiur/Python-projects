import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    )
""")

users_data = [
    ('Jakub', 'pass123', 'Jakub Kowalczyk', 15, 'kowalczyk@email.com'),
    ('Adrian', '123456', 'Adrian Nowak', 18, 'nowacki@email.com'),
    ('Michal', 'kichal', 'Michał Złoto', 27, 'michal@email.com')
]

cursor.executemany(
    "INSERT INTO users (username, password, name, age, email) VALUES (?, ?, ?, ?, ?)",
    users_data
)

conn.commit()
conn.close()
