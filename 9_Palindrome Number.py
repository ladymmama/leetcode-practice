class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        # coverted it to string
        a = str(x)[::-1]
        if a == str(x):
            return True
        else:
            return False
        """

        # math method

        if x < 0 or (x % 10 == 0 and x != 0):  # if x < 0, or its 10's mutilples
            return False
        rev = 0
        while x > rev:  # revert the string from  mid get the second half
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10
