#!/usr/bin/env python3

# the __all__ variable, that limits the list of imports, is only for this form of import!
from  module_foo import *

foo = Foo("gadget")
print(foo)

# not visible here, as print_foo is not listed in __all__ variable of the imported module!
#print_foo("some stuff: ", 42)


