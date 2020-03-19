class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        Min_Val = - 2 ** 31
        Max_Val = 2 ** 31 - 1

        flag = (dividend < 0) ^ (divisor < 0)  # check signal, same = 0, distinct = 1

        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while divisor <= dividend:
            temp = 1
            div = divisor
            while (div << 1) <= dividend:
                div <<= 1
                temp <<= 1
            dividend -= div
            ans += temp

            if ans >= Max_Val:
                if flag and ans == Max_Val + 1:
                    return Min_Val
                return Max_Val
        return ans if not flag else -ans
