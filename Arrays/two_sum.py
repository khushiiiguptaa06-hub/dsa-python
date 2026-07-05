"""
Problem: Two Sum

Approach: Hash Map

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums, target):
    """
    Returns indices of two numbers
    whose sum equals target.
    """

    hashmap = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i


if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))