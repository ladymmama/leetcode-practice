class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        a = ' '. join ((str.split())[::-1])
        return a