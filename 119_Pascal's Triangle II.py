class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] + [0] * rowIndex  # first initial the lengh and the first element for result.

        for i in range(rowIndex):
            res[0] = 1
            for j in range(i + 1, 0, -1):
                res[j] = res[j] + res[j - 1]
        return res