class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        res = []
        self.helper(nums, k, n, res, [], 0)
        return res

    def helper(self, nums, k, target, res, path, start):
        if target == 0 and k == 0:
            res.append(path)
        if target < 0:
            return
        for i in range(start, len(nums)):
            self.helper(nums, k - 1, target - nums[i], res, path + [nums[i]], i + 1)