import sqlite3

connect = sqlite3.connect('book_list.db')
cursor = connect.cursor()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Book(
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER
    );""")
    connect.commit()
    
    def display_books(self):
        cursor.execute('''SELECT * FROM Book''')
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год выпуска: {book[3]}")
        connect.commit()

    def add_book(self):
        cursor.execute(f'''INSERT INTO Book(title, author, year)
                       VALUES("{self.title}", '{self.author}', '{self.year}');''')
        
        connect.commit()

    def delete_book(self, title):
        cursor.execute('''DELETE FROM Book WHERE title = ?''', (title,))
        connect.commit()

    


        
book = Book('12','12',12) 
book.display_info()
book.display_books()
book.add_book()
book.delete_book('12')


