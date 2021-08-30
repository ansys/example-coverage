"""
Only for testing purpose.
"""


def testing_function():
    """Testing function description.

    Examples
    --------
    The purpose of this example is testing.

    >>> testing_function()

    """
    return "testing"


class ClassAAA:
    """Class for testing purpose.

    Parameters
    ----------
    input : str, optional
        input string.

    Examples
    --------
    Instantiate a ClassAAA object.

    >>> class_aaa = ClassAAA("test")

    """
    @property
    def my_property_aaa(self):
        """Property for testing."""
        return self._my_property_aaa

    @my_property_aaa.setter
    def my_property_aaa(self, value):
        self._my_property_aaa = value

    def __init__(self, input):
        self._my_property_aaa = input

    def _private_method_aaa(self):
        """Private method"""
        pass

    def method_aaa(self):
        """Method for test.

        Examples
        --------
        >>> class_aaa = ClassAAA("test")
        >>> class_aaa.method_aaa()

        """
