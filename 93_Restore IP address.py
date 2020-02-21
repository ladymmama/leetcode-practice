class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:  # corner case if the len of the string is too long to be the ip address
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.append('.'.join(path))  # once there are 4parts, we join them as one possibility.
            return
        for i in range(1, 4):
            if i > len(s):
                continue
            number = int(s[:i])  # 001 should not be valid. so we use int() to convert it to actual num
            if str(number) == s[
                              :i] and number <= 255:  # str() to make sure its not 001 something and number has to less than 255
                self.dfs(s[i:], path + [s[:i]], res)  # do the dfs for the rest to get all possibilities
