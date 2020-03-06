class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        if len(nums) <= 2:
            return len(nums)
        prev, curr = 1, 2
        while curr < len(nums):
            if nums[prev] == nums[curr] and nums[prev] == nums[prev - 1]:
                curr = curr + 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev+1
        """
        if len(nums) <= 2:
            return len(nums)
        j = 1
        for i in range(2, len(nums)):
            if not(nums[i] == nums[j] and nums[j] == nums[j-1]):
                j += 1
                nums[j] = nums[i]
        return j + 1