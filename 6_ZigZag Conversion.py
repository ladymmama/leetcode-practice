class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # TC:O(n), SC:O(n)
        if numRows == 1 or numRows >= len(s):
            return s
        row = 0
        step = 1

        res = ["" for _ in range(len(s))]
        for cha in s:
            res[row] += cha

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return "".join(res)  # SC:O(n)
