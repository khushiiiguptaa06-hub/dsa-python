"""
Problem: Largest Element in an Array
Approach: Single Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_largest(arr):
    """
    Returns the largest element in the array.
    """
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    arr = [5, 3, 7, 8, 2]
    print(find_largest(arr))