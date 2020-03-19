class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TC: O(n), SC: O(1)
        res = 0
        for num in nums:
            count = 0
            while num > 0:
                num //= 10
                count += 1
            if count % 2 == 0:
                res += 1
        return res
