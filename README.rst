ansys-tools-example-coverage
----------------------------
The ``ansys-tools-example-coverage`` library is intended to assess and report the docstring examples coverage
of modules and submoldules from a given directory.
example-coverage is licensed under the `MIT License
<https://github.com/pyansys/example-coverage/blob/main/LICENSE>`_.


What does this library do?
--------------------------
``ansys-tools-example-coverage`` displays the number of documentation strings containing
examples following either the `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_ or
`Google-Style <https://google.github.io/styleguide/pyguide.html>`_.

Example usage:

.. code::

    python -m ansys.tools.example_coverage -f "path_to_package"

    Name                                      Methods     Missed   Covered
    -----------------------------------------------------------------------
    my_package.my_module_a.sub_module_a             3          3       0.0%
    my_package.my_module_a.sub_module_b             6          3      50.0%
    my_package.my_module_a.sub_module_c             1          0     100.0%
    my_package.my_module_b                          4          1      75.0%
    -----------------------------------------------------------------------
    Total                                          14          7        50%

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
