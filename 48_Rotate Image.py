class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        # choose 1/4 parts, and rotate the whole image
        # TC: O(n*m) , SC: O(1)
        n = len(matrix) - 1
        for i in range(len(matrix)//2):
            for j in range(i, n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = temp
        """

        # first flip with y = row/2 , up and down switch?
        # then flip with y = x
        # TC:O(n^2), SC: O(1)
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row // 2):
            for j in range(col):
                matrix[i][j], matrix[row - 1 - i][j] = matrix[row - 1 - i][j], matrix[i][j]

        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]