import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 3, 0, -1]) == 3

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest is first."""
    assert longest_positive_streak([1, 2, 3, 4, 0, 1, 2]) == 4

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest is last."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 4]) == 4

def test_streaks_with_negatives_and_zeros():
    """Test streaks separated by zeros and negative numbers."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 0, 1]) == 3

def test_list_with_only_zero():
    """Test a list containing only a zero."""
    assert longest_positive_streak([0]) == 0

def test_long_list():
    """Test with a longer list of numbers."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 4, 5, -5, 1]) == 5