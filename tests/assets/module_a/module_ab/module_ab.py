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


class ClassAB:
    """Class for testing purpose.

    Parameters
    ----------
    input : str, optional
        input string.

    Examples
    --------
    Instantiate a ClassAB object.

    >>> class_ab = ClassAB("test")

    """

    # Property without example
    @property
    def my_property_ab(self):
        """Property for testing without example."""
        return self._my_property_ab

    @my_property_ab.setter
    def my_property_ab(self, value):
        self._my_property_ab = value

    # Property with example
    @property
    def my_property_ab_with_example(self):
        """Property for testing with example

        Examples
        --------
        >>> pass

        """
        return self._my_property_ab_with_example

    @my_property_ab_with_example.setter
    def my_property_ab_with_example(self, value):
        self._my_property_ab_with_example = value

    def __init__(self, input, second_input):
        self._my_property_ab = input
        self._my_property_ab_with_example = second_input

    def _private_method_ab(self):
        """Private method"""
        pass

    def method_ab(self):
        """Method for test.

        Examples
        --------
        >>> class_ab = ClassAB("test")
        >>> class_ab.method_ab()

        """
