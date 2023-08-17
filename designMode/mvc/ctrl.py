import view
from model import Person
'''
充当视图和模型之间的中介。监听由视图触发的事件，并为之查询模型。
'''
def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)

def start():
    view.startView()
    input = input()
    if input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    # running controller function
    start()