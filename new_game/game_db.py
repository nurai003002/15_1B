import sqlite3

connect = sqlite3.connect('gamer.db')
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS player(
               id INTEGER PRIMARY KEY,
               name VARCHAR (100),
               nick_name VARCHAR (100),
               age INTEGER,
               souses TEXT
);""")
connect.commit()

class Person:
    def __init__(self):
        self.name = None
        self.nick_name = None
        self.age = 0
        self.souses = None

    def registration(self, name, nick_name, age):
        self.name = name
        self.nick_name = nick_name
        self.age = age

        cursor.execute(f""" INSERT INTO player(name, nick_name, age)
                       VALUES ('{name}', '{nick_name}', '{age}')""")
        connect.commit()

    def hi(self):
        print('РЕГИСТРАЦИЯ')
        print('Откройте свой личный кабинет')
        name = input('Введите свое имя: ')
        nick_name = input('Введите свой никнейм: ')
        age = int(input('Введите свой возраст: '))
        self.registration(name, nick_name, age)
    
    
