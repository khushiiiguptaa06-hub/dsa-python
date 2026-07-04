"""
Problem: Best Time to Buy and Sell Stock

Approach: Running Minimum

Time Complexity: O(n)
Space Complexity: O(1)
"""

def best_time_to_buy_and_sell_stock(prices):
    """
    Finds the maximum profit by buying and selling
    the stock only once.

    Uses the Running Minimum pattern.
    """

    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]

    print("Maximum Profit:", best_time_to_buy_and_sell_stock(prices))