class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        d = {}
        res = 0

        for i in range(len(s)):
            if s[i] in d and d[s[
                i]] > start:  # if the char repeat after the last start, we update the start, and give this repeat value the new index
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i  # add the new one in dic
                if i - start > res:  # compare the max value
                    res = i - start
        return res