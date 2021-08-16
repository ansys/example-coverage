import ast
import os
import sys
import glob
import argparse
import pathlib

def find_files(folder_path):
    module_extension = ('.py')
    modules = []
    # for file in glob.glob(os.path.join(folder_path, '*.py')):
    #     if file.endswith(module_extension) & (not file.endswith("__init__.py")):
    #         modules.append(file)

    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if name.endswith(module_extension) & (not name.endswith("__init__.py")):
                modules.append(os.path.join(path,name))

    return modules

def create_report(folder_path):
    print(f'{"Name": <43}{"Methods":>12}{"Missed":>11}{"Covered":>10}')
    print ('-' * 79)

    all_methods_with_example = {}
    all_methods_without_example = {}

    for file in find_files(r'D:\GitHub\pyaedt\pyaedt'):
        with open(file) as fd:
            file_contents = fd.read()
        tree = ast.parse(file_contents)

        missing_functions = []
        covered_functions = []
        func_definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
        for func in func_definitions:
            if (ast.get_docstring(func) is None) or ("Example" not in ast.get_docstring(func)):
                missing_functions.append(func.name)
            else:
                covered_functions.append(func.name)

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
        if len(method_definitions)!=0:
            for method in method_definitions[0]:
                if (ast.get_docstring(method) is None) or ("Example" not in ast.get_docstring(method)):
                    missing_methods.append(method.name)
                else:
                    covered_methods.append(method.name)


        # WRITE REPORT
        all_methods_without_example[file] = missing_functions + missing_classes + missing_methods
        all_methods_with_example[file] = covered_functions + covered_classes + covered_methods

        missing = len(all_methods_without_example[file])
        total = missing + len(all_methods_with_example[file])

        covered = total - missing
        if total!=0:
            percentage_covered = covered/total*100
        else:
            # If no docstring is available in the module, coverage is considered to be 100%.
            percentage_covered = 100

        #module_name = file.split("C:\\Users\\mrey\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\html\\")[1].replace(os.path.sep, ".")
        module_name = os.path.basename(folder_path) + pathlib.Path(file.split(folder_path)[1].replace(os.path.sep, ".")).stem

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
    parser.add_argument('-f', '--folder',
        help='path of the package to perform coverage analysis on')
    # parser.add_argument('-r', '--recurse', default=True, type = bool,
    #     help='specify whether to recurse into submodules or not')
    args = parser.parse_args()
    create_report(args.folder)