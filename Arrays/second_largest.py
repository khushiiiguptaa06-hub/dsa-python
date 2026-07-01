"""
Problem: Second Largest Element in an Array
Approach: Optimal Single Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_second_largest(arr):
    """
    Returns the second largest distinct element in the array.
    """
    largest = float("-inf")
    second_largest = float("-inf")
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(find_second_largest(arr))