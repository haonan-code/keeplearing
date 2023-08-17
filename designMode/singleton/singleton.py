'''
将一个类的实例化限制为一个对象。它是一种创建模式，只涉及一个类来创建方法和指定对象。
'''
class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self) -> None:
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

# 三次获取到的对象都是同一个实例，说明单例模式确保了只有一个实例存在