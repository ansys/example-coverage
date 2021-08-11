Introduction
------------
example-coverage is intended to assess and report the docstring examples coverage
of modules and inner submoldules.
example-coverage is licensed under the `MIT License:
<https://github.com/pyansys/example-coverage/blob/main/LICENSE>`_.


What is example-coverage?
---------------
example-coverage is used to find every modules in a python package.
An option allows to discover each inner submodules included in the parent modules.
Then, every modules discovered in the previous task will be parsed to know if
examples are part or not of the docstring.
Finally a report will be written. It will list the covering percentage for every modules
analyzed.


Issues
------------------------
To post issues, questions, and code, go to `example-coverage Issues
<https://github.com/pyansys/example-coverage/issues>`_.


Connect to Desktop from Python IDE
----------------------------------
PyAEDT works both inside AEDT and as a standalone application.
It automatically detects whether it is running in an IronPython or CPython
environment and initializes the Desktop accordingly. PyAEDT also provides
advanced error management. Usage examples follow.

Analyze a module and all the submodules it contains.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bat

    python example_coverage -p"path_to_pacakge\\__init__.py"


Name                                      Methods     Missed   Covered
-------------------------------------------------------------------------------
my_package.moduleA.submolduleA                3          3       0.0%
my_package.moduleA.submolduleA                6          3      50.0%
my_package.moduleA.submolduleA                1          0     100.0%
my_package.moduleB                            4          1      75.0%
-------------------------------------------------------------------------------
Total                                        14          7        50%


License
-------
example-coverage is licensed under the MIT license.

This example-coverage module makes no commercial claim over Ansys whatsoever.