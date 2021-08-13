import ast
import os
import sys


def find_files(folder_path):
    module_extension = ('.py')
    modules = []
    for path, subdirs, files in os.walk(os.path.dirname(folder_path)):
    for name in files:
        if name.endswith(module_extension) & (not name.endswith("__init__.py")):
    return modules



ast_filename = r'D:\GitHub\pyaedt\pyaedt\hfss.py'

with open(ast_filename) as fd:
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
for method in method_definitions[0]:
    if (ast.get_docstring(method) is None) or ("Example" not in ast.get_docstring(method)):
        missing_methods.append(method.name)
    else:
        covered_methods.append(method.name)

