class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])

        # first we just need to ouput the first row
        res = matrix[0]
        if row > 1:  # if there is more than one row
            for i in range(1, row):
                res.append(matrix[i][col - 1])  # append the value from top to buttom

            if col > 1:  # if there is more than 1 col, we can go from right to left
                for j in range(col - 2, -1, -1):  # append the value from right to left in the last row
                    res.append(matrix[row - 1][j])

                for i in range(row - 2, 0,
                               -1):  # then we go from the second last row to the second row to append the value
                    res.append(matrix[i][0])

        M = []  # We create a matrix to store the rest value. And do recursion again.
        for k in range(1, row - 1):
            t = matrix[k][1:col - 1]
            M.append(t)

        return res + self.spiralOrder(M)
