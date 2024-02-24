from game_db import Person
person = Person()
user = input('У вас есть кабинет: "да","нет": ')
if user == 'да':
    from begin import dough
    dough()
else:
    person.hi()
    from begin import dough
    dough()
    

from sous import sauce
sauce()

