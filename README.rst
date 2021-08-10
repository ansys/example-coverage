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

Explicit Desktop declaration and error management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Launch AEDT 2021 R1 in Non-Graphical mode

    from pyaedt import Desktop, Circuit
    with Desktop("2021.1", NG=True):
        circuit = Circuit()
        ...
        # Any error here will be caught by Desktop.
        ...

    # Desktop is automatically released here.


License
-------
example-coverage is licensed under the MIT license.

This example-coverage module makes no commercial claim over Ansys whatsoever.