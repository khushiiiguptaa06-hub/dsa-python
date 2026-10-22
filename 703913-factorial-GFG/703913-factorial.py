class Solution:
    def factorial(self, n: int) -> int:
        # code here
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna