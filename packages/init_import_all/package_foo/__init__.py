

# upon import of this package, the __init__.py file is run in order to determine the interface of the package.
# include all modules here, these will be visible to the importer of the package.

import os as _os
import importlib as _importlib

def _import_all():

    # for each file in th package directory
    for file in _os.listdir( _os.path.join( _os.path.dirname(__file__) ) ):

        # get file components
        split = _os.path.splitext( file )

        # get basename of file
        base = split[-2]

        # import files with extension .py, but not __init__.py
        if split[-1] == '.py' and base != "__init__":

            # import module with from the current package.
            mod_var = _importlib.import_module( '.' + base, __package__)

            # merge the 'namepace' of the imported module with the current module
            for sym, val in mod_var.__dict__.items():
                # do not import private symbols.
                if sym[:1] != "_":
                    # add the symbol to the current namespace
                    globals().update({ sym :  val})


                if sym == "__all__":
                    if not "__all__" in globals():
                        globals()["__all__"] = []
                    globals()["__all__"] += val



_import_all()
