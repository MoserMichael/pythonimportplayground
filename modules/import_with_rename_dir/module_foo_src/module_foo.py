
# often done in modules. the import of datetime is used as _datetime; 
# when the module is imported, then this import will appear as a 'private' member variable of the import variable.
# pylint discourages you from using it in the context of the caller.
import datetime as _datetime
import os as _os

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "hello: %s, today is the %s" % (self.name, _datetime.date.today().ctime())


def print_foo(*args):
    print("module-foo says: ", " ".join(map(str, args)))

def _internal_print(*args):
    print("internal-foo says: ", " ".join(map(str, args)))

print("module_foo is being imported. Current directory: ", _os.getcwd())

