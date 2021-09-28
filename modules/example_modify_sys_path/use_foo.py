#!/usr/bin/env python3

import sys

sys.path.append("another_root")

print("modified sys.path: ", sys.path)

print("before: import module_foo")
import module_foo
print("after: import module_foo")

print(type(module_foo))
foo = module_foo.Foo("gadget")
print(foo)

module_foo.print_foo("some stuff: ", 42)

# it is possible to call an internal method exported by the module, but it is a bad thing to do.
# it gives you a bad pylint warning. Don't do that at home.
module_foo._internal_print("some stuff: ", 42)

print("")
print("module_foo.__dict__ keys: ", ", ".join(module_foo.__dict__.keys()))

for key, value in module_foo.__dict__.items():
    print("module_foo.__dict__ key: ", key, "value-type: ", type(value))

print("module_foo.__file__ : ", module_foo.__file__)
print("module_foo.__name__ : ", module_foo.__name__ )
print("module_foo.__package__ : ", module_foo.__package__)
print("module_foo.__cached__ : ", module_foo.__cached__)
print("module_foo.__loader__ : ", type(module_foo.__loader__) )



