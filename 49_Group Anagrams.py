class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for word in strs:
            reword = "".join(sorted(word))
            d[reword].append(word)
        return d.values()

