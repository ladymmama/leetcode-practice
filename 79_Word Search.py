class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # TC: O(m*n*4^l), SC: O(m*n+l)
        r = len(board)
        c = len(board[0])
        d = collections.defaultdict()
        for i in range(r):
            for j in range(c):
                if self.helper(word, 0, i, j, board):
                    return True
        return False

    def helper(self, word, index, row, col, board):
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False

        board[row][col] = "0"
        found = self.helper(word, index + 1, row + 1, col, board) or self.helper(word, index + 1, row - 1, col,
                                                                                 board) or self.helper(word, index + 1,
                                                                                                       row, col + 1,
                                                                                                       board) or self.helper(
            word, index + 1, row, col - 1, board)

        board[row][col] = word[index]

        return found
