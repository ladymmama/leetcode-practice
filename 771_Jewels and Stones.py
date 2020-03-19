class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # TC: O(n), SC: O(1)
        res = 0
        je = set(list(J))
        for i in S:
            if i in je:
                res += 1
        return res
    