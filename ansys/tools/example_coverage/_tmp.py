"""Notes taken with Alex"""

import importlib.util
import glob
import os
import pathlib

# from ansys.tools.example_coverage import example_coverage
# import ansys.tools.example_coverage

module_name = 'html'
module = __import__(module_name)

module_path = os.path.dirname(module.__file__)


def import_from_file(source_file):
    """Import a source file as a python module"""

    # get module name
    module_name = pathlib.Path(os.path.basename(source_file)).stem

    # execute module
    spec = importlib.util.spec_from_file_location(module_name, source_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

modules = {}

# loop through all attributes in the source file
for source_file in glob.glob(os.path.join("C:\\Users\\mrey\\AppData\\Local\\Programs\\Python\\Python38\\lib\\html", '*.py')):
    if "__init__.py" in source_file:
        continue
    module = import_from_file(source_file)
    modules[module.__name__] = module
    for attr in dir(module):
        if not attr.startswith('_'):
            item = getattr(module, attr)
            if callable(item):
                pass
                #breakpoint()
                # do something with __doc__
breakpoint()