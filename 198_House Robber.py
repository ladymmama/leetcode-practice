class Solution:
    def rob(self, nums: List[int]) -> int:
        last, curr = 0, 0

        for num in nums:
            last, curr = curr, max(curr, last + num)
        return curr

