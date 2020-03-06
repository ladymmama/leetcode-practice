class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC:O(m*n) SC:O(1)
        r = len(matrix)
        c = len(matrix[0])
        zero_r = False
        zero_c = False
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    zero_r = True if i == 0 else zero_r
                    zero_c = True if j == 0 else zero_c

        for i in range(1, r):  # fill the marked row
            if matrix[i][0] == 0:
                for j in range(1, c):
                    matrix[i][j] = 0

        for j in range(1, c):  # fill the marked col
            if matrix[0][j] == 0:
                for i in range(1, r):
                    matrix[i][j] = 0

        if zero_r:  # fill the first row and col if they marked as true
            for j in range(c):
                matrix[0][j] = 0
        if zero_c:
            for i in range(r):
                matrix[i][0] = 0
        # also there is another solution is TC:O(m*n) and SC:O(m+n)
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        """