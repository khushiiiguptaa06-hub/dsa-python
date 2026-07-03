"""
Problem: Union of Two Sorted Arrays

Pattern: Two Pointers (Compare Two Arrays)

Approach:
Use two pointers to compare elements of both sorted arrays.
Append only unique elements to the result.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


def union(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:

            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])

            i += 1

        elif arr1[i] > arr2[j]:

            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])

            j += 1

        else:

            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])

            i += 1
            j += 1

    while i < len(arr1):

        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])

        i += 1

    while j < len(arr2):

        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])

        j += 1

    return result


if __name__ == "__main__":

    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 3, 5]

    print("Union :", union(arr1, arr2))