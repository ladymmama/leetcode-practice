class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        d = collections.Counter(nums)  # create a hashmap to store every element and their count

        if k < 0:
            return 0

        for num in set(nums):
            if k > 0 and num + k in d:  # if num+k is in dict, it means there is a pair
                count += 1
            elif k == 0 and d[
                num] > 1:  # if k == 0 and there is more than one num[i], means we have the same number in a pair.
                count += 1

        return count