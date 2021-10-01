import datetime
import os

__all__ = [ "Foo" ]

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "hello: %s, today is the %s" % (self.name, datetime.date.today().ctime())


def print_foo(*args):
    print("module-foo says: ", " ".join(map(str, args)))

def _internal_print(*args):
    print("internal-foo says: ", " ".join(map(str, args)))

print("module_foo is being imported. Current directory: ", os.getcwd())
