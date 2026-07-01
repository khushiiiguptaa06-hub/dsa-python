"""
Problem: Check if Array is Sorted
Approach: Single Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_sorted(arr):
    """
    Returns True if the array is sorted in non-decreasing order,
    otherwise returns False.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(is_sorted(arr))