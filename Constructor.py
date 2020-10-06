'''
Constructor :   used to initialize objects
                same name as class

                syntax:
                        def __init__(self):

                        #body of cons

                ex:

                    def init(self,a,b) #default parameters

                    '''
class Maths:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        print("Calling constructor")

obj = Maths('Siva',123)
print(obj.name)
print(obj.number)

print(''' --------------- \n Another Example\n''')

class Math1:
    def __init__(abc,v,v1):
        abc.v = v
        abc.v1 = v1

    def show(abc):
        print(abc.v)
        print(abc.v1)

    def add(abc):
        return abc.v + abc.v1

obj1 = Math1(2343,421)
obj1.show()
print(obj1.add())

      



      
