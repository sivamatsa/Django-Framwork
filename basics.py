#class is collection of variables and methods
#blueprint for object

class Hello:
    a = 10
    b = 20

#method: function inside class
    def display():
        print("Hello I am function inside Class")

#user defined function
    def sum(a,b):
        return a+b
    
Hello.display()         #calling function
print(Hello.a ,Hello.b)

#object : instance of class 
s = Hello.sum(12,2)
print(s)


'''
OOP:

    programme is devided into objects
    more secure compared to procedural
    makes use of Acess Modifiers - Public , Private , Protected
    supports inheritece , polymorhism , ..
    

POP:

    Programme is devided into functions
    vice versa-- opposite to oop
'''
