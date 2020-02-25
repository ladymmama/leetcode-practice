class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:  # if this number greater than 0, then no need to find anything to right
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:  # if nums[i] + other two maxnumber number still less than 0
                continue  # no need to loop
            if 0 < i and nums[i] == nums[i - 1]:  # if i = 0,we should keep, otherwise, if they have the same number
                continue  # dont need to loop again

            l = i + 1  # left from i+1, right from the last element
            r = n - 1

            while l < r:  # when left < right
                temp = nums[i] + nums[l] + nums[r]

                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[
                        l + 1]:  # if the nums[l]==nums[l+1], move the left to next index
                        l += 1
                    while l < r - 1 and nums[r] == nums[
                        r - 1]:  # if the nums[r] == nums[r-1], shift the right to one step to the left
                        r -= 1
                    l += 1  # move the left to the right
                    r -= 1  # move the right to the left
                elif temp < 0:
                    l += 1
                else:
                    r -= 1

        return res
