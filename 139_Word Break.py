class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:  # corner case, if nothing,
            return False  # we return a false
        return self.dp(s, {}, wordDict)  # then we start dp

    def dp(self, s, mem, wd):
        if s == '':  # if there is an empty string, we return True
            return True
        if s in mem:  # if mem already record the s, we return bool s
            return mem[s]
        if s in wd:  # if s in dict, it can be the break
            mem[s] = True
            return True

        for i in range(len(s)):  # go over the whole string
            if s[:i] in wd and self.dp(s[i:], mem, wd):  # if the first part is in dict, we do the same operation with the right part
                mem[s] = True  # if its true, it means this string is valid.
                return True

        mem[s] = False  # after finishing the loop, if there is no match, we return False to indicates it cant divided.
        return False