class MathOperations:
    x,y,z = 10,39,40

    def sumNumbers():
        return MathOperations.x+MathOperations.y+MathOperations.z
    def mulNumbers():
        return MathOperations.x*MathOperations.y*MathOperations.z


#print(MathOperations.sumNumbers())    

obj = MathOperations
print(obj.sumNumbers())
print(obj.mulNumbers())
