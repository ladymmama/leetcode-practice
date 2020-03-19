class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # TC: O(n^2), SC: O(n)
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    res[i] += 1
        return res