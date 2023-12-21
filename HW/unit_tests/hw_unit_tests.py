import pytest


class CompareAverages:
    """Class for comparing the average values of two lists.

    Attributes:
        list1 (list)
        list2 (list)

    Methods:
        calculate_average(lst): Calculate the average value of a list.
        compare_averages(): Compare the average values of two lists.

    Magic Methods:
        __repr__()
        __str__()
        __lt__(other)
        __gt__(other)
        __eq__(other)

    """
    def __init__(self, list1, list2):
        """Initialize two lists"""
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """Calculate the average value of a given list.

        Args:
            lst (list): The input list of numbers.

        Returns:
            float: The average value of the list.
        """
        return sum(lst) / len(lst) if len(lst) > 0 else 0

    def compare_averages(self):
        """Compare the average values of two lists and determine which one is greater.

        Returns:
            str: A string indicating the result of the comparison.
        """
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)

        if average1 > average2:
            return "The first list has a greater average value"
        if average2 > average1:
            return "The second list has a greater average value"
        else:
            return "The average values are equal"

    def __repr__(self):
        """String representation of the CompareAverages object.

        Returns:
            str: A string representation of the object.
        """
        return f"CompareAverages(list1={self.list1}, list2={self.list2})"

    def __str__(self):
        """String representation of the CompareAverages object.

        Returns:
            str: A human-readable string representation of the object.
        """
        return f"Lists for comparison: {self.list1}, {self.list2}"

    def __lt__(self, other):
        """Less than comparison based on average values.

        Args:
            other (CompareAverages): Another CompareAverages object for comparison.

        Returns:
            bool: True if the average value of the current object is less than the other.
        """
        return self.calculate_average(self.list1) < other.calculate_average(other.list1)

    def __gt__(self, other):
        """Greater than comparison based on average values.

        Args:
            other (CompareAverages): Another CompareAverages object for comparison.

        Returns:
            bool: True if the average value of the current object is greater than the other.
        """
        return self.calculate_average(self.list1) > other.calculate_average(other.list1)

    def __eq__(self, other):
        """Equality comparison based on average values.

        Args:
            other (CompareAverages): Another CompareAverages object for comparison.

        Returns:
            bool: True if the average values of both objects are equal.
        """
        return self.calculate_average(self.list1) == other.calculate_average(other.list1)


# Test data...
@pytest.mark.parametrize("list1, list2, expected_result", [
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "The second list has a greater average value"),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "The average values are equal"),
    ([-1, -2, -3, -4, -5], [6, 7, 8, 9, 10], "The second list has a greater average value"),
    ([], [6, 7, 8, 9, 10], "The second list has a greater average value"),
    ([], [], "The average values are equal"),
])
def test_compare_averages(list1, list2, expected_result):
    """Test the comparison of average values between two lists.

    Args:
        list1 (list)
        list2 (list)
        expected_result (str)
    """
    comparison = CompareAverages(list1, list2)
    assert comparison.compare_averages() == expected_result


@pytest.fixture
def lst_positive():
    """Fixture for a list of positive integers."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def lst_negative():
    """Fixture for a list of negative integers."""
    return [-1, -2, -3, -4, -5]


@pytest.fixture
def lst_float():
    """Fixture for a list of float numbers."""
    return [1.5, 2.5, 3.5, 4.5, 5.5]


@pytest.fixture(autouse=True)
def lst_lists(lst_positive, lst_negative, lst_float):
    """Fixture to clean up lists after each test."""
    yield
    lists_to_cleanup = [lst_positive, lst_negative, lst_float]
    for list_fixture in lists_to_cleanup:
        del list_fixture[:]


# Test cases...
def test_compare_averages_positive_vs_negative(lst_positive, lst_negative):
    """Test the comparison of average values between a list of positive integers and a list of negative integers.

    Args:
        lst_positive (list): The list of positive integers.
        lst_negative (list): The list of negative integers.
    """
    comparison = CompareAverages(lst_positive, lst_negative)
    assert comparison.compare_averages() == "The first list has a greater average value"


def test_compare_averages_positive_vs_float(lst_positive, lst_float):
    """Test the comparison of average values between a list of positive integers and a list of floating-point numbers.

    Args:
        lst_positive (list): The list of positive integers.
        lst_float (list): The list of floating-point numbers.
    """
    comparison = CompareAverages(lst_positive, lst_float)
    assert comparison.compare_averages() == "The second list has a greater average value"


def test_comparison_operators_with_float(lst_float, lst_positive):
    """Test the comparison operators with lists of floating-point numbers and positive integers.

    Args:
        lst_float (list): The list of floating-point numbers.
        lst_positive (list): The list of positive integers.
    """
    comparison1 = CompareAverages(lst_float, lst_positive)
    comparison2 = CompareAverages([2.5, 3.5, 4.5, 5.5, 6.5], [7.5, 8.5, 9.5, 10.5, 11.5])

    assert comparison1 < comparison2
    assert not comparison1 > comparison2
    assert comparison1 != comparison2


def test_comparison_repr(lst_positive, lst_negative):
    """Test the string representation of the CompareAverages object.

    Args:
        lst_positive (list): The list of positive integers.
        lst_negative (list): The list of negative integers.
    """
    comparison = CompareAverages(lst_positive, lst_negative)
    assert repr(comparison) == f"CompareAverages(list1={lst_positive}, list2={lst_negative})"


def test_comparison_str(lst_positive, lst_negative):
    """Test the human-readable string representation of the CompareAverages object.

    Args:
        lst_positive (list): The list of positive integers.
        lst_negative (list): The list of negative integers.
    """
    comparison = CompareAverages(lst_positive, lst_negative)
    assert str(comparison) == f"Lists for comparison: {lst_positive}, {lst_negative}"


def test_comparison_operators(lst_positive, lst_negative):
    """Test the comparison operators with lists of positive and negative integers.

    Args:
        lst_positive (list): The list of positive integers.
        lst_negative (list): The list of negative integers.
    """
    comparison1 = CompareAverages(lst_positive, lst_negative)
    comparison2 = CompareAverages([2, 3, 4, 5, 6], [7, 8, 9, 10, 11])

    assert comparison1 < comparison2
    assert not comparison1 > comparison2
    assert comparison1 != comparison2


if __name__ == "__main__":
    pytest.main()
