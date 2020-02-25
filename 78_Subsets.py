class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # if needed, we can sort nums by nums.sort()
        if not nums:
            return [[]]
        if len(nums) == 1:  # if there is only one element, so subset is empty set and it self.
            return ([[], [nums[0]]])

        prev = self.subsets(nums[:-1])  # define the prev answer
        curr = []
        for item in prev:  # all sets' sub set = prev set + every item in the prev set + the new element
            curr.append(item + [nums[-1]])
        res = prev + curr
        return res