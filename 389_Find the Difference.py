class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in t:
            if j not in d:
                return j
            elif d[j] == 0:
                return j
            else:
                d[j] -= 1