from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix_sum = 0
        count = 0

        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in prefix_count:
                count += prefix_count[prefix_sum - goal]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count