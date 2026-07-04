"""
Problem: Leaders in an Array

Approach 1: Brute Force (Nested Loops)
Approach 2: Optimal (Traverse from Right)

Time Complexity:
    - Brute Force: O(n²)
    - Optimal: O(n)

Space Complexity:
    - O(k), where k is the number of leaders
"""


def leaders(arr):
    """
    Returns all leaders in the array using
    right-to-left traversal.
    """

    max_right = arr[-1]
    result = [arr[-1]]

    for i in range(len(arr) - 2, -1, -1):

        if arr[i] > max_right:
            result.append(arr[i])
            max_right = arr[i]

    result.reverse()

    return result


if __name__ == "__main__":

    arr = [10, 22, 12, 3, 0, 6]

    print("Leaders:", leaders(arr))