class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board) or not len(board[0]):
            return
        r = len(board)
        c = len(board[0])
        q = []
        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r - 1 or j == 0 or j == c - 1) and board[i][j] == "O":
                    q.append((i, j))

                    while q:
                        x, y = q.pop(0)
                        if (x < r and x >= 0 and y >= 0 and y < c) and board[x][y] == "O":
                            board[x][y] = "T"
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                q.append((x + dx, y + dy))

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"
