"""
Problem: Missing Number

Approach: Mathematical Formula

Time Complexity: O(n)
Space Complexity: O(1)
"""


def missing_number(arr):
    """
    Finds the missing number from the range 0 to n
    using the mathematical sum formula.
    """

    n = len(arr)
    actual_sum = sum(arr)
    expected_sum = n * (n + 1) // 2

    missing = expected_sum - actual_sum

    return missing


if __name__ == "__main__":

    arr = [3, 0, 1]

    print("Missing Number :", missing_number(arr))