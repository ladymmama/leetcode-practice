class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # TC: O(N*2^N) SC: O(N*2^N)
        res = []
        nums.sort()
        self.helper(nums, 0, res, [])
        return res

    def helper(self, nums, start, res, path):
        if path not in res:
            res.append(path)

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.helper(nums, i + 1, res, path + [nums[i]])