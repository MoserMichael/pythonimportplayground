
__all__ = [ "print_foo" ]

def print_foo(*args):
    print("module-foo says: ", " ".join(map(str, args)))

print("file2 is being imported")

