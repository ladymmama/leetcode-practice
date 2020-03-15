class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # TC：O(N^2 * log(N)), SC: O(N)
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for len_ in range(1, n + 1):
            for left in range(1, n - len_ + 2):
                right = left + len_ - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right],
                                          dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][
                                              right])
        return dp[1][n]

