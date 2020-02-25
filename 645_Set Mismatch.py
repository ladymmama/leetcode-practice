class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        # hashmap
        d = collections.Counter(nums)
        res = []
        dup, miss = 0, 0
        for i in range(1, len(nums)+1):
            if d[i] == 2:
                dup = i
            if i not in d:
                miss = i
        return [dup, miss]

        """

        # first solution is use math skill
        N = len(nums)
        nset = set(nums)
        missing = N * (N + 1) / 2 - sum(nset)  # missing = the result should be - sum(after remove duplicate)
        duplicated = sum(nums) - sum(nset)  # duplicate value = sum(nums) - sum(after remove duplicate nums)
        return [duplicated, missing]