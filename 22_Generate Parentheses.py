class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, tmp, res):
        if right < left:
            return

        if left == 0 and right == 0:
            res.append(tmp)

        if left > 0:
            self.helper(left - 1, right, tmp + '(', res)
        if right > 0:
            self.helper(left, right - 1, tmp + ')', res)
