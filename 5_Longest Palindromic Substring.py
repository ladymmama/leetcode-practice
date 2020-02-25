class Solution:
    def longestPalindrome(self, s):
        res = ''

        for i in range(len(s)):

            if len(res) < len(self.helper(s, i, i)):  # if the length of the result is smaller we update it.
                res = self.helper(s, i, i)

            if len(res) < len(self.helper(s, i, i + 1)):
                res = self.helper(s, i, i + 1)

        return res

    def helper(self, s, l, r):  # helper function to check if its palindromic.
        while l >= 0 and r < len(s) and s[l] == s[
            r]:  # when left is >= 0 or right is less than len(s), if they are equal
            l -= 1  # we increse the boundary.
            r += 1
        return s[l + 1:r]  # When quit the loop, we can return the last valid string.
