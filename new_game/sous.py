import sqlite3

connect = sqlite3.connect('gamer.db')
cursor = connect.cursor()

def player(user, new_nickname):
    cursor.execute("UPDATE player SET souses = ? WHERE nick_name = ?", (user, new_nickname))
    connect.commit()

def sauce():
    new_nickname = input('Введите свой никнейм: ')
    print('Ввиды соусов')
    print('томантный, сырный, чесночный')
    user = input('Ввыберите соус: ')
    if user == 'томантный':
        print('Тесто с томатным соусом готово' )
    elif user == 'сырный':
        print('Тесто с сырный соусом готово' )
    elif user == 'чесночный':
        print('Тесто с чесночный соусом готово' )
    player(user, new_nickname)

# qwww
    