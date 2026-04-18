import sqlite3

def create_table(conn):
    conn.execute("""
    DROP TABLE students
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students
    VALUES (?, ?, ?)
    """, (name, age, city))
    conn.commit()

def get_all_students(conn):
    result = conn.execute("""
    SELECT * FROM students
    """)
    return result.fetchall()