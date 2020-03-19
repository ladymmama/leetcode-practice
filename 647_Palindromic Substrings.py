class Solution:
    def countSubstrings(self, s: str) -> int:
        # TC: O(2n), SC: O(1)
        if not s:
            return 0

        self.res = 0
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
        return self.res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1
