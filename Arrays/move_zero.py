"""
Problem: Move Zeroes
Approach: Two Pointer (In-Place)

Time Complexity: O(n)
Space Complexity: O(1)
"""


def move_zeroes(nums):
    """
    Moves all zeroes to the end while maintaining
    the relative order of non-zero elements.

    Uses the Two Pointer technique.
    """

    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]

    print("Original Array      :", arr)
    print("After Move Zeroes   :", move_zeroes(arr))