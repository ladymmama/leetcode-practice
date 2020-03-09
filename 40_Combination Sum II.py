class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.helper(candidates, target, 0, res, [])
        return res

    def helper(self, nums, target, start, res, path):
        if target < 0:
            return
        if target == 0 and path not in res:
            res.append(path)

        for i in range(start, len(nums)):
            if nums[i] > target:
                return
            self.helper(nums, target - nums[i], i + 1, res, path + [nums[i]])