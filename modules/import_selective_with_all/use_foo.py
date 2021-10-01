#!/usr/bin/env python3

# for this form of import the __all__ variable is ignored.
from  module_foo import print_foo, Foo

foo = Foo("gadget")
print(foo)

print_foo("some stuff: ", 42)


