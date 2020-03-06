class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        for x in range(len(nums)):
            if nums[x] != x + 1:
                return x + 1

        return len(nums) + 1

    # we should store the value nums[i] at i-1's position
    # TC: O(2n) = O(n) SC: O(1)

