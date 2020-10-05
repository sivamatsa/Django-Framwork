class Student:
    
    #constructor
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        return {'name': self.name,'rollno':self.rollno}

obj = Student('Siva',513)
print(obj.display())


'''
Inheritance :  Getting Properties of one class to another class

Syntax:
        class subClass(parentClass1,[parentClass2,..]):
            functions

        class sub():

'''

class Cse:
    def student():
        return 'I am Cse Student'
class Ece:
    def student():
        return 'I am Ece Student'

obj1 = Cse
print(obj1.student())

obj2 = Ece
print(obj2.student())





