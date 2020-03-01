class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)  # we intialize the dp inifinity with size (0-amount) total is amount + 1
        dp[0] = 0  # intialize 0, if the amount is 0, we need 0 coin

        for coin in coins:  # compare each coin
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)  # find the minimal coin need for smaller value.
        return dp[amount] if dp[amount] != float("inf") else -1  # get the result for final amount