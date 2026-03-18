import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student_grades.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
""")

# Insert some dummy data
data = [
    (1, "Reinaldo", "Math", 95, "A"),
    (2, "Maria", "Math", 78, "C"),
    (3, "Luis", "History", 88, "B"),
    (4, "Ana", "History", 92, "A"),
    (5, "Antonio", "Science", 85, "B"),
    (6, "Isabel", "Math", 65, "D")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES (?, ?, ?, ?, ?)", data)
connection.commit()
connection.close()

print("Database created and populated successfully!")

