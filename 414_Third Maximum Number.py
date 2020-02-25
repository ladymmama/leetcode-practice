class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

        """

        nums_set = set(nums)

        if len(nums_set) < 3:
            return max(nums_set)
        else:
            nums_set.remove(max(nums_set))
            nums_set.remove(max(nums_set))
            _max = max(nums_set)
            return _max