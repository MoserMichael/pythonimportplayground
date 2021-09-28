#!/usr/bin/env python3

# as mfoo - module_foo will now be represented by variable mfoo, all access to module is via mfoo
import module_foo as mfoo

print(type(mfoo))
foo = mfoo.Foo("gadget")
print(foo)

mfoo.print_foo("some stuff: ", 42)

# it is possible to call an internal method exported by the module, but it is a bad thing to do.
# it gives you a bad pylint warning. Don't do that at home.

mfoo._internal_print("some stuff: ", 42)

print("")
print("mfoo.__dict__ keys: ", ", ".join(mfoo.__dict__.keys()))

for key, value in mfoo.__dict__.items():
    print("mfoo.__dict__ key: ", key, "value-type: ", type(value))

print("mfoo.__file__ : ", mfoo.__file__)
print("mfoo.__name__ : ", mfoo.__name__ )
print("mfoo.__package__ : ", mfoo.__package__)
print("mfoo.__cached__ : ", mfoo.__cached__)
print("mfoo.__loader__ : ", type(mfoo.__loader__) )





