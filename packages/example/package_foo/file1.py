
import datetime as _datetime

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "hello: %s, today is the %s" % (self.name, _datetime.date.today().ctime())

print("file1 is being  imported")
