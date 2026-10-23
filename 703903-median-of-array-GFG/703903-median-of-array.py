class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        mid = n // 2

        if n % 2 == 1:
            return arr[mid]
        else:
            return (arr[mid - 1] + arr[mid]) / 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna