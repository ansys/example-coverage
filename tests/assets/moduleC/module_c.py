"""
Only for testing purpose.
"""

def testing_fucntion():
    """Testing function description.

    Examples
    --------
    The purpose of this example is testing.

    >>> testing_function()

    """
    return "testing


class ClassC:
    """Initializes AEDT based on the inputs provided.

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
        """Current version of AEDT."""
        return self.my_property

    def __init__(self, input):
        self.my_property = input

    def _private_method_c(self):
        """Private method"""
        # Do nothing.

    def method_c(self):
        """Method for test.

        Examples
        --------
        >>> class_c = ClassC("test")
        >>> class_c.method_c()

        """
