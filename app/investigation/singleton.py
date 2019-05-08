
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print('--------------------')
        print(cls)
        print(cls._instances)
        print('--------------------')
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):

    def __init__(self,value) :
        print('*********ENTRO AL CONTRUCTOR*********')
        self.value = value



class MyClass2(metaclass=Singleton):
    pass

a = MyClass('valor 1')
b = MyClass('valor 2')
print(a)
print(a.value)
print(b)
print(b.value)


print('++++++instanciando otra clase++++++++')

c = MyClass2()
d = MyClass2()
print(c)
print(d)
