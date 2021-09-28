# The Python3 import playground


Sources:

    https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
    https://abarker.github.io/understanding_python_imports/ 
    https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
    https://docs.python.org/3/reference/import.html
    https://stackoverflow.com/questions/43059267/how-to-do-from-module-import-using-importlib

## modules 

Each file with extension .py can be used as a module. The module is in source file ```module_source.py```, while it is imported as ```import module_source```. It's easy, when both the module source file and the importing file are in the same directory.


### example module

- [source of a module_foo.py](https://github.com/mosermichael/pythonimportplayground/tree/master/modules/example_all_imports/module_foo.py) and example [using module_foo](https://github.com/mosermichael/pythonimportplayground/tree/master/modules/example_all_imports/module_foo.py) are in the same directory.
 
Lets import the module. (the module source includes a print statement ```print("module_foo is being imported")```)

```
>>> print("before: import module_foo")
before: import module_foo
>>> import module_foo
module_foo is being imported
>>> print("after: import module_foo")
after: import module_foo
```

The imported module is being parsed and run during the import statement. Python is a dynamic language, and there is no way to determine the interface of a module, without running it. This can have it's uses: you can add some module specific initialisations in the module, these are run just once at import time.

Often you can see the following lines in some python code:

```
if __name__ == '__main__':
  run_main_function()
```

This means that the function ```run_main_function``` will be run only when the file is run as a script (meaning it is run as ```python3 module_file.py```), __name__ is a built-in variable that holds the name of the current module, it defaults to "__main__" for file that is directly run by the python interpreter.

Interesting that even names with a leading underscore are visble via import (although pylint is giving a warning if you use them, and this is regarded as very bad style). Importing from a package does not expose these symbols.

How does the module look like on the importing side?

```
>>> import module_foo
>>>
>>> print(type(module_foo))
<class 'module'>
```

A variable with the same name as the imported module is defined implicitly by the python runtime, and it is of type ```<class 'module'>```. 

- lets use the interface that is exported by the module; all functions defined in the module are accessed via the module name followed by a dot.

```
foo = module_foo.Foo("gadget")
print(foo)

module_foo.print_foo("some stuff: ", 42)
```
- Lets take a look at the properties of the ```module_foo``` variable

```
>>> print("module_foo.__dict__ keys: ", ", ".join(module_foo.__dict__.keys()))
module_foo.__dict__ keys:  __name__, __doc__, __package__, __loader__, __spec__, __file__, __cached__, __builtins__, datetime, Foo, print_foo, _internal_print
```

This print statements shows all keys of the `___dict__``` member for the import module variable.
The ```__dict__``` member is a dictionary, and that one is listing all attributes of the module_foo variable. 

And the types of these members are just according to how they were defined in the module source files!

```
>>> for key, value in module_foo.__dict__.items():
...     print("module_foo.__dict__ key: ", key, "value-type: ", type(value))
...

module_foo.__dict__ key:  datetime value-type:  <class 'module'>
module_foo.__dict__ key:  Foo value-type:  <class 'type'>
module_foo.__dict__ key:  print_foo value-type:  <class 'function'>
module_foo.__dict__ key:  _internal_print value-type:  <class 'function'>
```

That makes sense: the call of  ```module_foo.print_foo("some stuff: ", 42)``` is just a short form for a regular object call ```module_foo.__dict__['module_foo'].print_foo("some stuff :", 42)``` An imported module is just an instance of a module object, where each exported class or method is just a member of that module object!

Please note: in this case ```module_foo``` is also listing all modules imported by the imported module (like module ```datetime```)

Now all symbols defined by the module (both classes and methods) are part of the __dict__ member of the import variable!.


### import renames.

There are other forms of import,

import module_foo as mfoo

Here the variable defined by the runtime is renamed to mfoo, and the code that uses the module looks as follows

mfoo.print_foo("some stuff: ", 42)

### import renames with directories.

The import with rename feature can be used to access python files in subdirectores: module_foo_src is in a sub directory, relative to  module_source.py

import module_foo_src.module_foo as mfoo

However some say that this kind of import does not make the code more readable. The [Google style guide](https://google.github.io/styleguide/pyguide.html#s2.2-imports) does not recommend this approach.

### importing symbols info the namespace of the caller

You can import symbols selectively into the calling program, as follows:

```
from  module_foo import print_foo, Foo

print_foo("some stuff: ", 42)

```
You can also import all symbols from module_foo right into your own namespace

```
from module_foo import *
```

### multiple imports

You can also import several packages from the same import statements, technically you can do

```
import os, sys as system, pathlib
```

However pylint gives you a warning for multiple imports in the same line, therefore it is not a good thing to do.

## packages

A Directory with an __init__.py is a python package, this directory can include more than one python file, the idea of a package is to treat all the python files in this directory as a whole. (you would get and error in python versions prior to 3.3)

Once a package is imported: its __init__.py in that directory is implicitly run, in order to determine the interface of that package.

An imported module foo must be a directory in the sys.path list, alternatively it can be a subdirectory of the current directory for a script.

```
>>> import sys
>>> print(sys.path)
['', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/Users/michaelmo/Library/Python/3.9/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']
```

The first entry is '', meaning the directory where the script file is in.

You can add directories to sys.path by setting PYTHONPATH environment variable, before running python exe, or by explicitly adding your directory to ```sys.path``, before calling import.

```
>>> import sys
>>> print(type(sys))
<class 'module'>
```

At the importing side: and imported module is represented by a variable of type 'class module'; the namespace of that module (including built-in classes and functions) are part of module_name.__dict__

import .. as - this construct is renaming the variable of type 'class module', to act as an alias for the import name.

```
>>> import sys as system
>>> print(system.path)
['', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/Users/michaelmo/Library/Python/3.9/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']
```

sys.modules - is a global variable, it's a dictionary that maps import name to variable of type <class 'module'>, It stands for$ all currently imported modules; import checks first if a modules is already imported,

```
>>> import sys
>>> print(sys.modules.keys())
dict_keys(['sys', 'builtins', '_frozen_importlib', '_imp', '_thread', '_warnings', '_weakref', '_io', 'marshal', 'posix', '_frozen_importlib_external', 'time', 'zipimport', '_codecs', 'codecs', 'encodings.aliases', 'encodings', 'encodings.utf_8', '_signal', 'encodings.latin_1', '_abc', 'abc', 'io', '__main__', '_stat', 'stat', '_collections_abc', 'genericpath', 'posixpath', 'os.path', 'os', '_sitebuiltins', '_locale', '_bootlocale', 'site', 'readline', 'atexit', 'rlcompleter'])
```

### packages

Here again is an example package. @@@


The tricky part in writing a package is the ```__init__.py``` , this file has to import all other files as modules, as follows:

```
from  .file1 import  *
```

This is a relative import, it imports the module file1 in file1.py from the current directory, and adds all symbols to the namespace of the __init__.py file (except for names with a leading underscore, these are treated as package private names). Having these symbols as part of the __init__.py namespace is the condition for making these symbols available upon import.

Technically, importing a package is the same to importing the __init__.py module of a package. It's the same as:

```
import package_name.__init__.py as package_dir
```

I sometimes forget to include a module from the __init__.py file, It is possible to include all modules from the same directory as the __init__.py file. See @@@ this example;  _import_all is a function that imports all modules in the same directory as __init__.py. It enumerates all files in that directory, it ignores all files with extenson other than .py and the  __init__.py. First, each python source file is loaded explicitly via ```importlib.import_module```, this function returns the module variable for the imported package.

Next, the namespace of that module is merged with the current namespace, it does so by enumerating all entries of the module variables ```__dict__`` member, and add these to the global namespace returned by the ```global()``` built-in function.



