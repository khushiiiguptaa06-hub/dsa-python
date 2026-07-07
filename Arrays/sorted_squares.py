"""
Problem: Squares of a Sorted Array (LeetCode 977)

Approach: Two Pointers

Time Complexity: O(n)
Space Complexity: O(n)
"""


def sorted_squares(nums):
    """
    Returns a sorted array of squares using the
    Two Pointer approach.
    """

    result = [0] * len(nums)

    left = 0
    right = len(nums) - 1
    pos = len(nums) - 1

    while left <= right:

        if nums[left] ** 2 > nums[right] ** 2:

            result[pos] = nums[left] ** 2
            left += 1

        else:

            result[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return result


if __name__ == "__main__":

    nums = [-4, -1, 0, 3, 10]

    print("Sorted Squares :", sorted_squares(nums))