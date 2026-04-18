import sqlite3


class Book:
    def __init__(self, name, author, publication_year, genre, number_of_pages, number_of_copies):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.number_of_pages = number_of_pages
        self.number_of_copies = number_of_copies


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
    connection.commit()
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
    Book("Лунная дорога", "Сабина Жээнбекова", 2013, "Драма", 270, 5)
]


if __name__ == "__main__":
    connection = sqlite3.connect("homeworks.db")

    create_table(connection)
    insert_books(connection, books)

    all_books = get_all_books(connection)

    connection.close()