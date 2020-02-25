class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # TC: O(n) SC: O(n)
        def helper(n):
            if n == 0:  #L0
                return ['0']
            if n == 1:  #L1
                return ['0', '1']
            res = helper(n-1)       # Ln-1 (previous sequence)
            return ['0' + s for s in res] + ['1' + s for s in res[::-1]] # 0.Ln-1 + 1.Ln-1(r)
        return [int(s, 2) for s in helper(n)] #change the base 2 to decimal number