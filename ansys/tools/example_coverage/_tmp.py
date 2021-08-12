"""Notes taken with Alex"""

import importlib.util
import glob
import os

from ansys.tools.example_coverage import example_coverage
import ansys.tools.example_coverage

module_name = 'html'
module = __import__(module_name)

module_path = os.path.dirname(module.__file__)


def import_from_file(source_file):
    """Import a source file as a python module"""
    spec = importlib.util.spec_from_file_location("_module", source_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# loop through all attributes in the source file
for source_file in glob.glob(os.path.join(module_path, '*.py')):
    module = import_from_file(source_file)
    for attr in dir(module):
        if not attr.startswith('_'):
            item = getattr(module, attr)
            if callable(item):
                breakpoint()
                # do something with __doc__
