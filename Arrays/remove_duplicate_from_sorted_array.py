"""
Problem: Remove Duplicates from Sorted Array
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(arr):
    """
    Removes duplicates from a sorted array in-place
    and returns the count of unique elements.
    """
    unique = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[unique]:
            unique += 1
            arr[unique] = arr[i]

    return unique + 1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3]
    k = remove_duplicates(arr)

    print("Unique Count:", k)
    print("Modified Array:", arr[:k])