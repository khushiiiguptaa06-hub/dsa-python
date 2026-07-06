"""
Problem: Reverse String (LeetCode 344)

Approach: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""


def reverse_string(arr):
    """
    Reverses the given character array in-place
    using the Two Pointer approach.
    """

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


if __name__ == "__main__":

    arr = list(input("Enter a string: "))

    reverse_string(arr)

    print("Reversed String :", "".join(arr))