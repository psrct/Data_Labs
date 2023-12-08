'''Exercise 00.04 - Person V.1'''

class Person:
    '''Person'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        '''Get details'''
        print("{0}, {1} years old".format(self.name, self.age))

    def say_hello(self):
        '''Say hello'''
        print("Hello, my name is %s!" %self.name)

def create_person():
    '''Create a new person'''
    person = Person(input(), int(input()))
    person.get_details()
    person.say_hello()

create_person()
