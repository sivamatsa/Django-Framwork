class File:
    ''' Pyton use Oop concepts and use Django
    framework for creating websites '''
    
    def feature():
        f = ['python','java','c','c++']
        return f
    def apps():
        a = ["web","ml","ai"]
        return a

obj = File
print(obj.feature())
print(obj.apps())
print(obj.__doc__)
