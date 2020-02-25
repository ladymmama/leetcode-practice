class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        low_price = float("inf")

        for price in prices:
            low_price = min(low_price, price)
            max_p = max(max_p, price - low_price)
        return max_p