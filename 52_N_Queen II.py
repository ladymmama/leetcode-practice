class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        self.count = 0
        self.dfs(0, n, [])  # start dfs on [0][0] positions
        return self.count

    def dfs(self, queens, n, positions):  # queens: list of the row number of the position
        if queens == n:  # if there are n queens means finish one possiblities
            self.count += 1  # we count this
            return
        for col in range(n):  # traverse every col
            if self.isSafe(queens, col, positions):  # if its safe position, we move to the next row
                self.dfs(queens + 1, n,
                         positions + [(queens, col)])  # and start to check if its valid in the next position
                # at the same time, add this position to the position list

    def isSafe(self, row, col, positions):
        for i in range(len(positions)):  # for each position, we check if :
            x, y = positions[i][0], positions[i][1]  # there are in the same col,(will not at the same row cause row = row + 1)
            if y == col or x - y == row - col or x + y == row + col:  # and if they are not on the diagnal
                return False
        return True