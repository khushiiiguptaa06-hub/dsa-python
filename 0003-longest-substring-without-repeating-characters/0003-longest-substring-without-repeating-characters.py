class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):

            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            last_index[ch] = right

            max_length = max(max_length, right - left + 1)

        return max_length