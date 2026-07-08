class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for num in range(k):
            window_sum += nums[num]
            max_sum = window_sum

        for num in range(k,len(nums)):
            window_sum = window_sum - nums[num-k] + nums[num]

            max_sum = max(max_sum, window_sum)
        return max_sum/k
        