import ast
import os
import sys
import argparse
import pathlib

def find_files(folder_path):
    """Find all modules available in the folder path provided.

    The selection is made based on the file's extension.
    However, __init__.py will be discarded.
    """

    # Raise an exception if the folder is empty.
    if os.listdir(folder_path):
        raise FileNotFoundError(f"There are no python source files in {folder_paths}.")

    modules = []

    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if name.endswith(".py") & (not name.endswith("__init__.py")):
                modules.append(os.path.join(path,name))

    # Raise an exception if none module was discovered in the input folder.
    if not modules:
        raise Exception(f"None module found in: {folder_path}.")

    return modules

def create_report(folder_path):
    """Write a report to list all modules and the docstring example
    coverage stats for each of these modules."""
    print(f'{"Name": <43}{"Docstrings":>12}{"Missed":>11}{"Covered":>10}')
    print ('-' * 79)

    # The key of those dictionaries will be the name of the file.
    # So we can easily extract specific information for every module.
    all_methods_with_example = {}
    all_methods_without_example = {}

    # Abstract tree structure is used to get all functions, classes, methods.
    for file in find_files(folder_path):
        with open(file) as fd:
            file_contents = fd.read()
        tree = ast.parse(file_contents)

        missing_functions = []
        covered_functions = []
        function_definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
        for function in function_definitions:
            # private function are not expected to provide any examples
            if function.name.startswith('_'):
                continue
            if (ast.get_docstring(function) is None) or ("Example" not in ast.get_docstring(function)):
                missing_functions.append(function.name)
            else:
                covered_functions.append(function.name)

        class_definitions = [node for node in tree.body if isinstance(node, ast.ClassDef)]

        method_definitions = []
        missing_classes = []
        covered_classes = []
        for class_def in class_definitions:
            method_definitions.append([node for node in class_def.body if isinstance(node, ast.FunctionDef)])
            if (ast.get_docstring(class_def) is None) or ("Example" not in ast.get_docstring(class_def)):
                missing_classes.append(class_def.name)
            else:
                covered_classes.append(class_def.name)

        missing_methods = []
        covered_methods = []
        if method_definitions:
            for method in method_definitions[0]:
                # Handle method with decorator.
                # Property setters should not have any example but getters do.
                property = False
                if method.decorator_list:
                    for decorator in method.decorator_list:
                        # Find property getter decorator.
                        if isinstance(decorator, ast.Name) and decorator.id == "property":
                            if ast.get_docstring(method) is None:
                                missing_methods.append(method.name)
                                property = True
                            elif "Example" not in ast.get_docstring(method):
                                missing_methods.append(method.name)
                                property = True
                            else:
                                covered_methods.append(method.name)
                                property = True
                        # Find property setter decorator.
                        elif isinstance(decorator, ast.Attribute) and decorator.attr == "setter":
                            # For setter methods, we consider them covered.
                            covered_methods.append(method.name)
                            property = True

                # If the method was a property, it has already been dealt with.
                # There is no need to continue the current method inspection.
                if property:
                    continue

                # Private methods are not expected to provide any examples.
                if method.name.startswith('_'):
                    continue
                if ast.get_docstring(method) is None or "Example" not in ast.get_docstring(method):
                    missing_methods.append(method.name)
                else:
                    covered_methods.append(method.name)

        # Write report.
        all_methods_without_example[file] = missing_functions + missing_classes + missing_methods
        all_methods_with_example[file] = covered_functions + covered_classes + covered_methods

        missing = len(all_methods_without_example[file])
        total = missing + len(all_methods_with_example[file])

        covered = total - missing
        if total:
            percentage_covered = covered/total*100
        else:
            # If no docstring is available in the module, coverage is considered to be 100%.
            percentage_covered = 100

        module_name = os.path.join(os.path.basename(folder_path), pathlib.Path(file.split(folder_path)[1].replace(os.path.sep, ".")).stem)

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

    if package_total!=0:
        package_percentage_covered = (package_total - package_missing) / package_total * 100
    else:
        # If none example is expected in the entire package, coverage is considered to be 100%.
        package_percentage_covered = 100
    print ('-' * 79)
    print(f'{"Total" : <43}{package_total : 12d}{package_missing : 11d}{package_percentage_covered:9.1f}%')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Evaluate example coverage of a package.')
    parser.add_argument('-f', '--folder',
        help='path of the package to perform coverage analysis on')
    args = parser.parse_args()
    create_report(args.folder)