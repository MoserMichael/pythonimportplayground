#!/usr/bin/env python3

import package_foo

print("")
print("package_foo.__dict__ keys: ", ", ".join(package_foo.__dict__.keys()))

for key, value in package_foo.__dict__.items():
    print("package_foo.__dict__ key: ", key, "value-type: ", type(value))
print("")


print(type(package_foo))
foo = package_foo.Foo("gadget")
print(foo)

package_foo.print_foo("some stuff: ", 42)

#unlike module import: private symbols from the package are not imported into the importing namespace
#package_foo._internal_print("some stuff: ", 42)

print("package_foo.__file__ : ", package_foo.__file__)
print("package_foo.__name__ : ", package_foo.__name__ )
print("package_foo.__package__ : ", package_foo.__package__)
print("package_foo.__cached__ : ", package_foo.__cached__)
print("package_foo.__loader__ : ", type(package_foo.__loader__) )



