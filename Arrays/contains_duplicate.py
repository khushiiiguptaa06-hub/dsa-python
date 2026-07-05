"""
Problem: Contains Duplicate

Approach: Hash Set

Time Complexity: O(n)
Space Complexity: O(n)
"""


def contains_duplicate(nums):
    """
    Returns True if any value appears at least twice.
    """

    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


if __name__ == "__main__":

    nums = [1, 2, 3, 1]

    print(contains_duplicate(nums))