class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums [i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1    


        """
        Do not return anything, modify nums in-place instead.
        """
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna