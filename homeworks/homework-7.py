import sqlite3


class Book:
    def __init__(self, name, author, publication_year, genre, number_of_pages, number_of_copies):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.number_of_pages = number_of_pages
        self.number_of_copies = number_of_copies

# Сделал drop_table чтобы мне было удобно отслеживать таблицу просто

def drop_table(connection):
    connection.execute("""
    DROP TABLE IF EXISTS books
    """)

def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    print("Таблица books создана")


def insert_books(connection, books):
    for book in books:
        connection.execute("""
        INSERT INTO books
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            book.name,
            book.author,
            book.publication_year,
            book.genre,
            book.number_of_pages,
            book.number_of_copies
        ))
        print(f"Книга {book.name} успешно добавлена")
    connection.commit()


def get_all_books(connection):
    result = connection.execute("""
    SELECT * FROM books
    """)
    return result.fetchall()


def get_books_by_author(conn, author: str):
    result = conn.execute("""
    SELECT * FROM books WHERE author = ?
    ORDER BY name ASC
    """, (author,))
    return result.fetchall()

books = [
    Book("Тайна старого маяка", "Алина Ветрова", 2015, "Детектив", 320, 7),
    Book("Пески времени", "Марат Исаков", 2018, "Фантастика", 410, 5),
    Book("Зимний сад", "Елена Соколова", 2020, "Роман", 280, 10),
    Book("Город теней", "Игорь Невский", 2017, "Ужасы", 350, 4),
    Book("Последний рубеж", "Данияр Касымов", 2021, "Боевик", 390, 6),
    Book("Секрет небес", "Виктория Ланская", 2019, "Фэнтези", 500, 8),
    Book("Шаг до мечты", "Ольга Миронова", 2016, "Мотивация", 230, 12),
    Book("Подводный мир", "Руслан Токтосунов", 2014, "Приключения", 300, 3),
    Book("Код будущего", "Артем Беликов", 2022, "Научная фантастика", 450, 9),
    Book("Лунная дорога", "Сабина Жээнбекова", 2013, "Драма", 270, 5),
    Book("История бурмалды", "Артем Беликов", 2021, "Классика", number_of_pages=300, number_of_copies=6)
]


if __name__ == "__main__":
    connection = sqlite3.connect("homeworks.db")
    drop_table(connection)
    create_table(connection)

    print(get_all_books(connection))
    print(get_books_by_author(connection, "Артем Беликов"))
    connection.close()