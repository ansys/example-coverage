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


class ClassC:
    """Class for testing purpose.

    Parameters
    ----------
    input : str, optional
        input string.

    Examples
    --------
    Instantiate a ClassC object.

    >>> class_c = ClassC("test")

    """
    @property
    def my_property_c(self):
        """Property for testing."""
        return self._my_property_c

    @my_property_c.setter
    def my_property_c(self, value):
        self._my_property_c = value

    def __init__(self, input):
        self._my_property_c = input

    def _private_method_c(self):
        """Private method"""
        pass

    def method_c(self):
        """Method for test.

        Examples
        --------
        >>> class_c = ClassC("test")
        >>> class_c.method_c()

        """
