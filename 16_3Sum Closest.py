class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float("inf")
        nums.sort()
        n = len(nums)

        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if abs(_sum - target) < abs(res - target):
                    res = _sum

                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    return target

        return res
