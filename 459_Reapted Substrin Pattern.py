class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)/2 + 1):
            if len(s) % i:  # if the length is not the multiple of i, no result.
                continue
            elif s[:i] * (len(s) / i) == s: # if there is a mutilple, and s[:i] * max number for this parttern == s
                return True     # its true
        return False # otherwise return false