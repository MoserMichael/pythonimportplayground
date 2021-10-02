#!/usr/bin/env python3
import sys

print("before: import package_foo")
from package_foo import *
print("after: import package_foo")

# this trick gets the module variable for the current module
this_module = sys.modules[ __name__ ]

print("")
print("for this module: __dict__ keys: ", ", ".join(this_module.__dict__.keys()))

# without making a copy of the dict, it tells me that the container changed during iteration
for key, value in dict(this_module.__dict__).items():
    print("this_module.__dict__ key: ", key, "value-type: ", type(value))
print("")


print(type(this_module))
foo = Foo("gadget")
print(foo)

print_foo("some stuff: ", 42)

#unlike module import: private symbols from the package are not imported into the importing namespace
#_internal_print("some stuff: ", 42)

print("this_module.__file__ : ", this_module.__file__)
print("this_module.__name__ : ", this_module.__name__ )
print("this_module.__package__ : ", this_module.__package__)
print("this_module.__cached__ : ", this_module.__cached__)
print("this_module.__loader__ : ", type(this_module.__loader__) )

# for * imports the __all__ variable is not propagated
#print("this_module.__all__ : ", this_module.__all__ )




