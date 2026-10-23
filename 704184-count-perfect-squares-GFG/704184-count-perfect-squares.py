class Solution:
    def countSquares(self, n):
        # code here 
        
        count = 0
        for i in range(1,n):
            if i * i < n:
                count += 1
            else:
                break
        return count    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna