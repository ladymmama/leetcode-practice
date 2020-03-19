class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # TC: O(n), SC:O(1)
        res = 0
        l_count = 0
        r_count = 0
        for item in s:
            if item == "L":
                l_count += 1
            if item == "R":
                r_count += 1

            if l_count == r_count:
                res += 1
                l_count = 0
                r_count = 0
        return res
