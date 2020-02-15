class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        c = col - 1 #start from top rightmost
        while r < row and c >= 0: #traverse the whole matrix
                if matrix[r][c] == target: #if topright most equal to target
                    return True
                if matrix[r][c] < target:  #if smaller than target, move to next row
                    r += 1
                else: #if greater than target, move to the left col
                    c -= 1
        return False
