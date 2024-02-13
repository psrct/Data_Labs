'''Labs 10.01 Student Class'''

class Student:
    '''Class Student'''
    def __init__(self, std_id, name, gpa):
        '''init'''
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self):
        '''get std_id'''
        return self.__std_id

    def get_name(self):
        '''get name'''
        return self.__name

    def get_gpa(self):
        '''get gpa'''
        return self.__gpa

    def print_detail(self):
        '''print details'''
        print("ID: {}\nName: {}\nGPA: {:.2f}".format(self.get_std_id(),
                                                     self.get_name(), self.get_gpa()))

def main(text_in):
    '''Main'''
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())
