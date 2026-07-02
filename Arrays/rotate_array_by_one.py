"""
Problem: Left Rotate Array by One Place
Approach 1: Pythonic (Using Slicing)
Approach 2: In-Place Rotation
Time Complexity: O(n)
Space Complexity:
    - Approach 1: O(n)
    - Approach 2: O(1)
"""


def left_rotate_pythonic(arr):
    """
    Returns a new array after left rotating by one place.
    Uses Python slicing.
    """
    return arr[1:] + [arr[0]]

def left_rotate_inplace(arr):
    """
    Left rotates the array by one place without using
    any extra space.
    """
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first
    return arr

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]

    print("Pythonic Approach :", left_rotate_pythonic(arr1))
    print("In-Place Approach :", left_rotate_inplace(arr2))