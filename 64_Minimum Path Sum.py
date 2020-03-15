class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # TC: O(m*n) SC:O(1)
        if not grid or not grid[0]:
            return 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j - 1]
                elif j == 0:
                    before = grid[i - 1][j]
                else:
                    before = min(grid[i - 1][j], grid[i][j - 1])

                grid[i][j] = before + grid[i][j]

        return grid[r - 1][c - 1]