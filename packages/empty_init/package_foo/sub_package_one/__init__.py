

# That funny single dot before module name is read as “current package”. That's a relative import.
# now import * means to get all symbols from the package, and add them to all currently available symbols of the __init__.py module.
# that's how they will become accessible in the importer of the package.

from  .file1 import  *



