class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        # TC: O(log n) SC:O(1)
        _len = len(nums)

        left = 0
        right = _len


        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left
        """
        # TC: O(n), SC: O(1)
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i