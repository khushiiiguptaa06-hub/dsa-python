"""
Problem: Merge Two Sorted Arrays

Approach: Three Pointers (Merge Step of Merge Sort)

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into a single sorted array.
    """

    ans = [0] * (len(arr1) + len(arr2))

    i = 0
    j = 0
    k = 0

    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            ans[k] = arr1[i]
            i += 1
            k += 1

        else:
            ans[k] = arr2[j]
            j += 1
            k += 1

    # Copy remaining elements of arr1
    while i < len(arr1):
        ans[k] = arr1[i]
        i += 1
        k += 1

    # Copy remaining elements of arr2
    while j < len(arr2):
        ans[k] = arr2[j]
        j += 1
        k += 1

    return ans


if __name__ == "__main__":

    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    print("Merged Array :", merge_sorted_arrays(arr1, arr2))