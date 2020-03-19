class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                k = j + 1
                l = n - 1
                rem = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] > rem:
                        l -= 1
                    elif nums[k] + nums[l] < rem:
                        k += 1

                    elif nums[k] + nums[l] == rem:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        while k + 1 < l and nums[k] == nums[k + 1]:
                            k += 1
                        while l - 1 > k and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                while j < n - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < n - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return res