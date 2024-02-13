'''Labs 10.02 ProbHash Hashing'''

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

class ProbHash:
    '''Class ProbHash'''
    def __init__(self, size):
        '''init'''
        self.__hash_table = size * [None]
        self.__size = size

    def hash_table(self):
        '''hash table'''
        return self.__hash_table

    def hash(self, key):
        '''hash key'''
        return key%self.__size

    def rehash(self, hkey):
        '''rehash key'''
        newkey = hkey
        while True:
            if newkey >= self.__size:
                return newkey
            elif self.hash_table()[newkey] == None:
                return newkey
            elif newkey == hkey - 1:
                return self.__size
            else:
                newkey = (newkey + 1) % self.__size

    def insert_data(self, std):
        '''insert_data'''
        hkey = self.hash(std.get_std_id())
        newkey = self.rehash(hkey)
        if newkey < self.__size:
            self.hash_table()[newkey] = std
            print("Insert {} at index {}".format(std.get_std_id(), newkey))
        else:
            print("The list is full. {} could not be inserted.".format(std.get_std_id()))

    def search_data(self, std_id):
        '''search_data'''
        indexx = self.hash(std_id)
        in2 = indexx
        while True:
            if in2 >= self.__size or in2 == indexx - 1:
                print("{} does not exist.".format(std_id))
                break
            elif self.hash_table()[in2] != None and self.hash_table()[in2].get_std_id() == std_id:
                print("Found {} at index {}".format(std_id, in2))
                self.hash_table()[in2].print_detail()
                break
            else:
                in2 = (in2 + 1) % self.__size

def main():
    '''Main'''
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
