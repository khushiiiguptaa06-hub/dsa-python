from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0

        prefix_count = {0: 1}

        for num in nums:

            if num % 2 == 1:
                prefix_sum += 1

            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count