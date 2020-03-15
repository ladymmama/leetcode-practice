class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        r_start, c_start = 0, 0
        r_end, c_end = n - 1, n - 1
        number = 1
        while r_start <= r_end and c_start <= c_end:
            for j in range(c_start, c_end + 1):
                res[r_start][j] = number
                number += 1
            r_start += 1

            for i in range(r_start, r_end + 1):
                res[i][c_end] = number
                number += 1
            c_end -= 1

            if r_start <= r_end:
                for k in range(c_end, c_start - 1, -1):
                    res[r_end][k] = number
                    number += 1
                r_end -= 1

            if c_start <= c_end:
                for l in range(r_end, r_start - 1, -1):
                    res[l][c_start] = number
                    number += 1
                c_start += 1

        return res