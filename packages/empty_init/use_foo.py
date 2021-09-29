#!/usr/bin/env python3

import package_foo.sub_package_one as sub_package_one
import package_foo.sub_package_two as sub_package_two


foo = sub_package_one.Foo("gadget")
print(foo)

sub_package_two.print_foo("some stuff: ", 42)




