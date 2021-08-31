import os
import sys
import io

import pytest

from ansys.tools.example_coverage import create_report


THIS_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIRECTORY = os.path.join(THIS_PATH, 'assets')


class CaptureStdOut():
    """Capture standard output with a context manager."""

    def __init__(self):
        self._stream = io.StringIO()

    def __enter__(self):
        sys.stdout = self._stream

    def __exit__(self, type, value, traceback):
        sys.stdout = sys.__stdout__

    @property
    def content(self):
        """Return the captured content."""
        return self._stream.getvalue()


def test_empty_folder():
    """ Provide a folder that does not contain any file or folder."""
    path = os.path.join(ASSETS_DIRECTORY, "empty_")

    with pytest.raises(Exception) as excinfo:
        create_report(path)
    assert "No python modules found in:" in str(excinfo.value)
    assert "empty_" in str(excinfo.value)


def test_empty_folder_non_recursiveness():
    """Ensure that no source files are returned when recursiveness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "empty_")

    with pytest.raises(Exception) as excinfo:
        create_report(path, False)
    assert "No python modules found in:" in str(excinfo.value)
    assert "empty_" in str(excinfo.value)


def test_only_init_module():
    """ Provide a folder that contains solely an __init__.py file."""
    path = os.path.join(ASSETS_DIRECTORY, "only_init")

    with pytest.raises(Exception) as excinfo:
        create_report(path)
    assert "No python modules found in: " in str(excinfo.value)
    assert "only_init" in str(excinfo.value)


def test_only_init_module_non_recursiveness():
    """ Provide a folder that contains solely an __init__.py file.
    Recusrviness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "only_init")

    with pytest.raises(Exception) as excinfo:
        create_report(path, False)
    assert "No python modules found in: " in str(excinfo.value)
    assert "only_init" in str(excinfo.value)


def test_package_a():
    """ The package tested is made of several modules and submodules."""
    path = os.path.join(ASSETS_DIRECTORY, "module_a")

    capture = CaptureStdOut()
    with capture:
        create_report(path)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_a.module_aa.module_aa                          5          1     80.0%
module_a.module_aa.module_aaa.module_aaa              5          1     80.0%
module_a.module_ab.module_ab                          7          1     85.7%
-------------------------------------------------------------------------------
Total                                                17          3     82.4%
"""


def test_package_a_non_recursiveness():
    """ The package tested is made of several modules and submodules.
    Recusrviness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "module_a")

    with pytest.raises(Exception) as excinfo:
        create_report(path, False)
    assert "No python modules found in: " in str(excinfo.value)
    assert "module_a" in str(excinfo.value)


def test_package_aa_non_recustiveness():
    """ The package tested is made of several modules and submodules."""
    path = os.path.join(ASSETS_DIRECTORY, "module_a", "module_aa")

    capture = CaptureStdOut()
    with capture:
        create_report(path, False)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_aa.module_aa                                   5          1     80.0%
-------------------------------------------------------------------------------
Total                                                 5          1     80.0%
"""


def test_package_b():
    """ The package tested is made of a single module.
    None __init__.py file is available.
    In this module, there is a single private function.
    So, none example is expected for this entire module."""
    path = os.path.join(ASSETS_DIRECTORY, "module_b")

    capture = CaptureStdOut()
    with capture:
        create_report(path)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_b.module_b                                     0          0    100.0%
-------------------------------------------------------------------------------
Total                                                 0          0    100.0%
"""


def test_package_b_non_recursiveness():
    """ The package tested is made of a single module.
    None __init__.py file is available.
    In this module, there is a single private function.
    So, none example is expected for this entire module.
    Recusrviness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "module_b")

    capture = CaptureStdOut()
    with capture:
        create_report(path, False)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_b.module_b                                     0          0    100.0%
-------------------------------------------------------------------------------
Total                                                 0          0    100.0%
"""


def test_package_c():
    """The package tested contains standard property. Recursiveness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "module_c")

    capture = CaptureStdOut()
    with capture:
        create_report(path)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_c.module_c                                     5          1     80.0%
-------------------------------------------------------------------------------
Total                                                 5          1     80.0%
"""


def test_package_c_non_recursiveness():
    """The package tested contains standard property."""
    path = os.path.join(ASSETS_DIRECTORY, "module_c")

    capture = CaptureStdOut()
    with capture:
        create_report(path, False)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_c.module_c                                     5          1     80.0%
-------------------------------------------------------------------------------
Total                                                 5          1     80.0%
"""


def test_package_d():
    """The package tested contains several decorators."""
    path = os.path.join(ASSETS_DIRECTORY, "module_d")

    capture = CaptureStdOut()
    with capture:
        create_report(path)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_d.module_d                                     8          3     62.5%
-------------------------------------------------------------------------------
Total                                                 8          3     62.5%
"""


def test_package_d_non_recursive():
    """The package tested contains several decorators. Recusrviness is disabled."""
    path = os.path.join(ASSETS_DIRECTORY, "module_d")

    capture = CaptureStdOut()
    with capture:
        create_report(path, False)

    assert capture.content == """Name                                         Docstrings     Missed   Covered
-------------------------------------------------------------------------------
module_d.module_d                                     8          3     62.5%
-------------------------------------------------------------------------------
Total                                                 8          3     62.5%
"""
