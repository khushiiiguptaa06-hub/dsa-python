"""
Problem: Left Rotate Array by K Places
Approach 1: Pythonic (Using Slicing)
Approach 2: Reversal Algorithm (In-Place)
Time Complexity: O(n)
Space Complexity:
    - Approach 1: O(n)
    - Approach 2: O(1)
"""


def left_rotate_by_k_pythonic(arr, k):
    """
    Returns a new array after left rotating
    the array by k places.
    """
    n = len(arr)
    k = k % n

    return arr[k:] + arr[:k]

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate_by_k_inplace(arr, k):
    """
    Left rotates the array by k places
    using the Reversal Algorithm.
    """
    n = len(arr)
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    k = 2

    print("Pythonic Approach :", left_rotate_by_k_pythonic(arr1, k))
    print("In-Place Approach :", left_rotate_by_k_inplace(arr2, k))