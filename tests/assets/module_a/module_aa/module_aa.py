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


class ClassAA:
    """Class for testing purpose.

    Parameters
    ----------
    input : str, optional
        input string.

    Examples
    --------
    Instantiate a ClassAA object.

    >>> class_aa = ClassAA("test")

    """
    @property
    def my_property_aa(self):
        """Property for testing."""
        return self._my_property_aa

    @my_property_aa.setter
    def my_property_aa(self, value):
        self._my_property_aa = value

    def __init__(self, input):
        self._my_property_aa = input

    def _private_method_aa(self):
        """Private method"""
        pass

    def method_aa(self):
        """Method for test.

        Examples
        --------
        >>> class_aa = ClassAA("test")
        >>> class_aa.method_aa()

        """
