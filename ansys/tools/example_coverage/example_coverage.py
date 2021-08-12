from doctest import DocTestFinder
from types import ModuleType
import os
import sys
import argparse
import importlib
import pathlib
import pkgutil

def get_module_from_package_name(package_path):

    # get the directory of the entry package
    directory_name = os.path.dirname(package_path)
    # return the name of the entry package
    module_name = os.path.basename(directory_name)

    sys.path.append(os.path.abspath(directory_name))
    spec = importlib.util.spec_from_file_location(module_name, package_path)
    # entry_module = importlib.util.module_from_spec(spec)

    entry_module = __import__(module_name)

    return entry_module


def get_modules(package_path):
    sys.path.append(os.path.dirname(package_path))
    module_extensions = ('.py')
    package_name = os.path.basename(os.path.dirname(package_path))
    modules = {}

    for path, subdirs, files in os.walk(os.path.dirname(package_path)):
        for name in files:
            if name.endswith(module_extensions) & (not name.endswith("__init__.py")):

                module_name = package_name + path.split(package_name)[-1].replace(os.path.sep, ".") + "." + pathlib.Path(name).stem

                # spec = importlib.util.spec_from_file_location(module_name, os.path.join(package_path, "__init__.py"))
                # module = importlib.util.module_from_spec(spec)
                module = __import__(module_name)
                modules[module.__name__] = module

    import pdb
    pdb.set_trace()
    return modules

def discover_modules(package_path, recurse=True):
    """Discover the submodules present under an entry point.

    If ``recurse=True``, search goes all the way into descendants of the
    entry point. Only modules are gathered, because within a module
    ``doctest``'s discovery can work recursively.

    Should work for ``pyaedt`` as entry, but no promises for its more
    general applicability.

    Parameters
    ----------
    package_path : str
        The path of the package to be analyzed for example coverage.
    recurse : bool, optional
        Whether to recurse into submodules.

    Returns
    -------
    modules : dict of modules
        A (module name -> module) mapping of submodules under ``entry``.

    """

    #module = get_module_from_package_name(package_path)

    import pdb
    pdb.set_trace()

    module = package_path

    entry_module = __import__(module.__name__)
    entry_name = entry_module.__name__
    found_modules = {}
    next_entries = [entry_module]

    while next_entries:
        next_modules = {}
        for entry_module in next_entries:
            for attribute in dir(entry_module):
                attribute_value = getattr(entry_module, attribute)
                if not isinstance(attribute_value, ModuleType):
                    continue

                module_name = attribute_value.__name__

                if module_name.startswith(entry_name):
                    next_modules[module_name] = attribute_value

        # Find as-of-yet-undiscovered submodules.
        next_entries = [
            module
            for module_name, module in next_modules.items()
            if module_name not in found_modules
        ]

        found_modules.update(next_modules)

        if not recurse:
            break

    # Remove the name package folders from the 'found_modules' dictionary.
    for key in list(found_modules.keys()):
        if found_modules[key].__file__.endswith("__init__.py"):
            del found_modules[key]

    import pdb
    pdb.set_trace()

    return found_modules

def list_module(package_path):
    modules = {}
    sys.path.append(package_path)
    for importer, modname, ispkg in pkgutil.walk_packages([package_path], os.path.basename(package_path) + '.'):
        module = __import__(modname)
        modules[modname] = module
    return modules

def evaluate_examples_coverage(package_path, recurse=True):
    """Check whether doctests can be run as-is without errors.

    Parameters
    ----------
    package_path : string
        The path of the package to be analyzed for example coverage.
    recurse : bool, optional
        Specify whether to recurse into submodules or not.
    """
    # Get the modules to analyze.
    if package_path is None:
        raise ValueError(f"{package_path} cannot be None. A package name must be provided")
    else:
        # import package_path
        #modules = discover_modules(package_path, recurse)
        modules = {}
        for importer, modname, ispkg in pkgutil.walk_packages([package_path], os.path.basename(package_path) + '.'):
            module = __import__(modname)
            modules[modname] = module

    import pdb
    pdb.set_trace()

    # Find and parse all docstrings.
    doctests = {}
    for module_name, module in modules.items():
        doctests[module_name] = {
            doctest.name: doctest
            for doctest in DocTestFinder(recurse=True).find(module, globs={})
            }

    import pdb
    pdb.set_trace()

    print(f'{"Name": <43}{"Methods":>12}{"Missed":>11}{"Covered":>10}')
    print ('-' * 79)

    # Those dictionaries can later be used to extract 
    # the name of the methods without example for each module.
    # This can be done easily because the keys of the dictionaries
    # are the module names.
    all_methods_with_example = {}
    all_methods_without_example = {}

    # Loop over doctests in alphabetical order for sanity.
    sorted_module_names = sorted(doctests)
    for module_name in sorted_module_names:
        methods_with_example = []
        methods_without_example = []

        for dt_name in doctests[module_name]:
            # Private methods should not be considered.
            if (not doctests[module_name][dt_name].examples) & (not dt_name.startswith("_")):
                methods_without_example.append(dt_name)
            else:
                methods_with_example.append(dt_name)

        all_methods_without_example[module_name] = methods_without_example
        all_methods_with_example[module_name] = methods_with_example

        total = len(doctests[module_name])
        missing = len(methods_without_example)
        covered = total - missing
        if total!=0:
            percentage_covered = covered/total*100
        else:
            # If no docstring is available in the module, coverage is considered to be 100%.
            percentage_covered = 100

        print(f'{module_name[:42]: <43}{total:12}{missing:11}{percentage_covered:9.1f}%')

    # Get the stats for the entire package.
    all_methods_with_example_list = []
    for method_list in list(all_methods_with_example.values()):
        all_methods_with_example_list.extend(method_list)

    all_methods_without_example_list = []
    for method_list in list(all_methods_without_example.values()):
        all_methods_without_example_list.extend(method_list)

    package_total = len(all_methods_with_example_list) + len(all_methods_without_example_list)
    package_missing = len(all_methods_without_example_list)
    package_percentage_covered = (package_total - package_missing) / package_total * 100
    print ('-' * 79)
    print(f'{"Total" : <43}{package_total : 12d}{package_missing : 11d}{package_percentage_covered:8.1f}%')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Evaluate example coverage of a package.')
    parser.add_argument('-p', '--package',
        help='name of the package to perform coverage analysis on')
    parser.add_argument('-r', '--recurse', default=True, type = bool,
        help='specify whether to recurse into submodules or not')
    args = parser.parse_args()
    evaluate_examples_coverage(args.package, args.recurse)