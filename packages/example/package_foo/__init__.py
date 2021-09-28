
print("start of running __init__")

# upon import of this package, the __init__.py file is run in order to determine the interface of the package.
# include all modules here, these will be visible to the importer of the package.

import os as _os

print("current directory in __init__.py, dir: ", _os.getcwd())


# That funny single dot before module name is read as “current package”. That's a relative import.
# now import * means to get all symbols from the package, and add them to all currently available symbols of the __init__.py module.
# that's how they will become accessible in the importer of the package.

from  .file1 import  *
from  .file2 import  * 

# that's the long form of doing the same import: with the name of current package.
#from  package_foo.file1 import *
#from  package_foo.file2 import *


__all__=[ "Foo" ]
print("from __init__,  __all__ : ", __all__)

print("end of running __init__")



