class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]

    # dp = [4,1,8,3], n = 4
    # for layer in (2,-1,-1):
    #   for i in (0,3):
    # layer: 2, i = 0: dp[0]= 1 + 6, i = 1: dp[1] = 1 + 5, dp[2] = 3 + 7
    # layer: 1, i = 0: dp[0]= 6 + 3, i = 1: dp[1] = 6 + 4
    # dp[0] =  9 + 2 = 11
    