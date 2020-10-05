class ClassA:
    def m1():
        return 'ClassA'

class ClassB(ClassA):
    def m2():
        return 'ClassB'
class ClassC(ClassB,ClassA):
    def m3():
        return 'ClassC'

obj = ClassA
obj1 = ClassB
obj2 = ClassC

print (obj.m1())
print (obj1.m2())
print (obj2.m3())

