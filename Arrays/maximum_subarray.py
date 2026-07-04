"""
Problem: Maximum Subarray

Approach: Kadane's Algorithm

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maximum_subarray(nums):
    """
    Finds the maximum sum of a contiguous subarray
    using Kadane's Algorithm.
    """

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Maximum Subarray Sum:", maximum_subarray(nums))