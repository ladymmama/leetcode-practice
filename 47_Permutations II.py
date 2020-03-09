class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            n = nums[:i] + nums[i+1:]
            for comb in self.permuteUnique(n):
                if [nums[i]] + comb not in res:
                    res.append([nums[i]] + comb)
        return res