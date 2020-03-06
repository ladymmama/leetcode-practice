class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        mat = [[1] * n] * m  # creat a m * n matrix
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[m - 1][n - 1]