class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # TC: O(n), SC:O(1)

        res = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            res += 1

        return res