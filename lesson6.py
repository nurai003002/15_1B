# CRUD- Create, Read, Update, Delete
# СУБД-Cистема Управления Базой Данных

import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customs(
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               surname VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL,
               email TEXT,
               balance DOUBLE (8, 2),
               is_active BOOLEAN DEFAULT FALSE
                            
);""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.email = None
        self.balance = 0
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name 
        self.surname = surname
        self.age = age
        self.email = email
        cursor.execute(f""" INSERT INTO customs (name, surname, age, email, balance, is_active)
                       VALUES('{name}', '{surname}', '{age}', '{email}', 0, True);""")
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f"""UPDATE customs SET balance = balance + {amount} WHERE email = '{self.email}' """)
        connect.commit()
        self.balance += amount
    
    def minus(self, amount):
        cursor.execute(f"""UPDATE customs SET balance = balance - {amount} WHERE email = '{self.email}' """)
        connect.commit()
        self.balance -= amount

    def main(self):
        while True:
            print("1 - Регистрация, 2 - Пополнение, 3 - Вывести деньги, 4 - выйти")
            command = int(input("Выберите действие: ")) 
            if command ==1:
                print('РЕГИСТРАЦИЯ')
                name = input('Введите ваше имя: ')
                surname = input('Введите фамилию: ')
                age = int(input('Введите ваш возраст: '))
                email = input("Введите вашу почту: ")
                self.register(name,surname,age, email)
                print('Вы успешно зарегистрировались ')
            
            elif command == 2: 
                if self.email:
                    print('ПОПОЛНЕНИЕ')
                    amount = int(input('Введите сумму: '))
                    self.deposit(amount)
                    print('Вы успешно пополнили баланс')
                else:
                    print('Пройдите регистрация')

            elif command == 3:
                if self.email:
                    print('ВЫВЕСТИ ДЕНЬГИ')
                    amount = int(input('Введите сумму для снятия: '))
                    self.minus(amount)
                    print('Вы успешно сняли сумму')

            elif command == 4:
                break

            else:
                print("1 - Регистрация, 2 - Пополнение, 3 - Вывести деньги, 4 - выйти")
                command = int(input("Выберите действие: ")) 
                
    

bank = Bank()
bank.main()



# INTEGER - int
# VARCHAR - str - (Строки с ограничением )
# TEXT - str - (без ограничения)
# BOOLEAN - bool 
# DOUBLE - float 
# NOT NULL - (поле не должен быть  пустым)
# DEFAULT - (по умолчанию)


