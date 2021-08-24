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


def testing_decorator(func):
    """Custom decorator for testing."""
    def wrapper(arg):
        func(arg)
    return wrapper


@testing_decorator
def call_decorator():
    pass


class ClassD:
    """Class for testing purpose.

    Parameters
    ----------
    input : str, optional
        input string.

    Examples
    --------
    Instantiate a ClassD object.

    >>> class_d = ClassD("test")

    """
    @property
    def my_property_d(self):
        """Property for testing."""
        return self._my_property_d

    @my_property_d.setter
    def my_property_d(self, value):
        self._my_property_d = value

    def __init__(self, input, second_input):
        self._my_property_d = input
        self._property_with_decorator = second_input

    def _private_method_d(self):
        """Private method"""
        pass

    @property
    @testing_decorator
    def property_with_decorator(self):
        """Property with additional decorator.

        Examples
        --------
        Property with additional decorator.

        >>> class_d = ClassD("first_arg", "second_arg")
        >>> class_d.property_with_decorator

        """
        return self._property_with_decorator

    def method_d(self):
        """Method for test.

        Examples
        --------
        >>> class_d = ClassD("first_arg", "second_arg")
        >>> class_d.method_d()

        """
