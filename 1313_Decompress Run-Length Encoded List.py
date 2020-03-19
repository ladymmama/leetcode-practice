class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # TC: O(n/2) = O(n), SC: O(1)
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i + 1]] * nums[i]

        return res
    