class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        res = []
        candidates.sort()
        self.helper(res, candidates, target, 0, [])
        return res

    def helper(self, res, array, target, start, path):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(start, len(array)):
            if array[i] > target:
                return
            self.helper(res, array, target - array[i], i, path + [array[i]])
