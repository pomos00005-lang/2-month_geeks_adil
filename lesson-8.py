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
        number_of_copies INTEGER
    )
    ''')
def insert_book(conn, name,author,publication_year,genre,number_of_pages,number_of_copies):
    conn.execute('''
    INSERT INTO books(name_book , author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    ''',
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def delete_book(conn, book_id):
    conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

def update_book_name(conn, book_id, new_name):
    conn.execute('UPDATE books SET name_book = ? WHERE id = ?', (new_name, book_id))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('books.db')
    create_table(conn)

    insert_book(conn, 'Война и мир', 'Лев Толстой', 1869, 'Роман', 1225, 10)
    insert_book(conn, 'Преступление и наказание', 'Фёдор Достоевский', 1866, 'Роман', 672, 7)
    insert_book(conn, 'Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', 480, 12)
    insert_book(conn, '1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 15)
    insert_book(conn, 'Гарри Поттер и философский камень', 'Дж. Ролинг', 1997, 'Фэнтези', 432, 20)
    insert_book(conn, 'Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Сказка', 96, 18)
    insert_book(conn, 'Отцы и дети', 'Иван Тургенев', 1862, 'Роман', 290, 6)
    insert_book(conn, 'Собака Баскервилей', 'Артур Конан Дойл', 1902, 'Детектив', 256, 9)
    insert_book(conn, 'Мёртвые души', 'Николай Гоголь', 1842, 'Роман', 352, 8)
    insert_book(conn, 'Алхимик', 'Пауло Коэльо', 1988, 'Притча', 208, 14)

    delete_book(conn, 1)
    update_book_name(conn,7,'ИЗМЕНИНО ')