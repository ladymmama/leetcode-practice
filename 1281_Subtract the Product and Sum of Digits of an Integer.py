class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TC: O(n), SC:O(1)
        if not n:
            return 0

        pro = 1
        s = 0
        while n > 0:
            digit = n % 10
            n //= 10
            pro *= digit
            s += digit

        return pro - s