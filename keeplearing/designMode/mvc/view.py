from model import Person
'''
视图代表HTML文件，它与终端用户进行交互。它向用户表示模型的数据。
'''
def showAllView(list):
    print('In our db we have %i user. Here they are:' % len(list))
    for item in list:
        print(item.name())

def startView():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')

def endView():
    print('Goodbye!')