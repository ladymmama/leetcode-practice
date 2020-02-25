class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.


        if k % len(nums) and len(nums) > 1:
            k = k % len(nums)
            temp = nums[-k:]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-k]
            nums[0:k] = temp

        return nums

        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

        # for this one, if we can find the rotate equalt to put the last k numbers in the front.
        return nums