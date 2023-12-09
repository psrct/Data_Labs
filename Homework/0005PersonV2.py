'''Exercise 00.05 - Person V.2'''

class Person:
    '''Person Class'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        '''Get details'''
        print("{}, {} years old".format(self.name, self.age))

    def say_hello(self):
        '''Say hello'''
        return "Hello, my name is {}!".format(self.name)

class Project:
    '''Project Class'''
    def __init__(self, name_project, num_members):
        self.project_name = name_project
        self.num_member = num_members

    def show_project_name(self):
        '''Show project name'''
        print("Hello There! This is {}".format(self.project_name))

    def show_members(self):
        '''Show members'''
        print("This project has {} members".format(self.num_member))
        listname = []
        for _ in range(self.num_member):
            person = Person(input(), int(input()))
            listname.append(person.say_hello())
            listname.sort(key=lambda x: x[:][18:])
        for i in listname:
            print(i)

def main():
    '''main fuction'''
    project = Project(input(), int(input()))
    project.show_project_name()
    project.show_members()

main()
