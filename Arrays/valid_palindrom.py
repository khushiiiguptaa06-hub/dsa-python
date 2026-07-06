"""
Problem: Valid Palindrome (LeetCode 125)

Approach: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""


def is_palindrome(s):
    """
    Returns True if the given string is a palindrome.
    Ignores spaces, punctuation, and letter case.
    """

    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":

    s = input("Enter a string: ")

    print("Is Palindrome :", is_palindrome(s))