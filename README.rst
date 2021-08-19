ansys-tools-example-coverage
----------------------------
The ``ansys-tools-example-coverage`` library is intended to assess and report the docstring examples coverage
of modules and submoldules from a given directory.
example-coverage is licensed under the `MIT License:
<https://github.com/pyansys/example-coverage/blob/main/LICENSE>`_.


What does this library do?
--------------------------
example-coverage is used to find every modules in a python package.
An option allows to discover each inner submodules included in the parent modules.
Then, every modules discovered in the previous task will be parsed to know if
examples are part or not of the docstring.
Finally a report will be written. It will list the covering percentage for every modules
analyzed.
Installation
------------
Install with:

.. code::

   pip install ansys-tools-example-coverage



Issues
------------------------
To post issues, questions, and code, go to `example-coverage Issues
<https://github.com/pyansys/example-coverage/issues>`_.



License
-------
``ansys-tools-example-coverage`` is licensed under the MIT license.
