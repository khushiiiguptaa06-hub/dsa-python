class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        for i in range(k):
            if s[i].lower() in "aeiou":
                vowel_count += 1
        max_count = vowel_count
        for i in range(k, len(s)):
            if s[i-k].lower() in "aeiou":
                vowel_count -=1
            if s[i].lower() in "aeiou":
                vowel_count += 1    
            max_count = max(max_count, vowel_count)
        return max_count                