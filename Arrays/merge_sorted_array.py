"""
Problem: Merge Sorted Array

Approach: Three Pointers (Traverse from Back)

Time Complexity: O(m + n)
Space Complexity: O(1)
"""


def merge_sorted_array(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 in-place.
    """

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:

        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


if __name__ == "__main__":

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    print(merge_sorted_array(nums1, m, nums2, n))