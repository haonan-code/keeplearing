import json
'''
由纯应用逻辑组成，与数据库进行交互。它包括所有的信息，向终端用户表示数据。
'''
class Person(object):
    def __init__(self, first_name = None, last_name = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
    def name(self):
        return("%s %s" % (self.first_name, self.last_name))
    
    @classmethod
    # returns all people inside db.txt as list of Person objects
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result
        