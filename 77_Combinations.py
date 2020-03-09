class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])  # all possible value for the res
        return res

    def helper(self, tmp, k, res, path):  # tmp1: [1,2,3,4]
        if k > len(tmp):  # there is not enough number to grab, return nothing
            return
        if k == 0:  # find a possibility, then add this path
            res.append(path)
        else:  # otherwise, choose the first one. and do the same opreation with the rest.
            for i in range(len(tmp)):
                self.helper(tmp[i + 1:], k - 1, res, path + [tmp[i]])


