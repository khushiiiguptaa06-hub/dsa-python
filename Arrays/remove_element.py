"""
Problem: Remove Element

Approach: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""


def remove_element(nums, val):
    """
    Removes all occurrences of val in-place
    and returns the count of remaining elements.
    """

    j = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return j


if __name__ == "__main__":

    nums = [3, 2, 2, 3]
    val = 3

    k = remove_element(nums, val)

    print("Remaining Count:", k)
    print("Modified Array:", nums[:k])
    