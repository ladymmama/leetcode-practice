class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        l = s.strip().split(" ")
        if not s:
            return 0
        return len(l[-1])
        """
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res += 1
            elif res > 0:
                break
        return res
        # TC:O(n), SC:O(1)
