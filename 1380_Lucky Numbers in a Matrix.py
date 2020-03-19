class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if self.max_col(matrix, r, c, i, j):
                    if self.min_row(matrix, r, c, i, j):
                        return [matrix[i][j]]

    def max_col(self, matrix, r, c, i, j):
        c_max = float("-inf")
        for x in range(r):
            c_max = max(c_max, matrix[x][j])
        if matrix[i][j] >= c_max:
            return True
        else:
            return False

    def min_row(self, matrix, r, c, i, j):
        r_min = float("inf")
        for y in range(c):
            r_min = min(r_min, matrix[i][y])
        if matrix[i][j] <= r_min:
            return True
        else:
            return False