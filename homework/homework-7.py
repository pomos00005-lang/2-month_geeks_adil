import sqlite3

def create_table(conn):
    conn.execute('DROP TABLE IF EXISTS books')
    conn.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_book TEXT NOT NULL,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_pages_of_author INTEGER
    )
    ''')
def insert_book(conn, name,author,publication_year,genre,number_of_pages,number_of_pages_of_author):
    conn.execute('''
    INSERT INTO books(name_book  , author, publication_year, genre, number_of_pages, number_of_pages_of_author)
    VALUES (?, ?, ?, ?, ?, ?)
    ''',
    (name, author, publication_year, genre, number_of_pages, number_of_pages_of_author)
    )
    conn.commit()
if __name__ == '__main__':
    conn = sqlite3.connect('books.db')
    create_table(conn)

    for i in range(int(input('Введите сколько книг вы хотите добавить в базу(минимум 10 книг): '))):
        insert_book(conn,
                    input('Enter name: '),
                    input('Enter author: '),
                    int(input('Enter publication year: ')),
                    input('Enter genre: '),
                    int(input('Enter number of pages: ')),
                    int(input('Enter number of copies: '))
                    )