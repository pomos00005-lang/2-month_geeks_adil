import sqlite3

def create_connection(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT      
    )    
    ''')
def add_student(conn, name, age, city):
    conn.execute('''
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    ''',
    (name, age, city))
    )
    conn.commit()
if __name__ == '__main__':
    conn = sqlite3.connect('student.db')
    create_connection(conn)