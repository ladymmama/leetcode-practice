class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)

        for c in "!?',;.":  # replace all those sign with space.
            paragraph = paragraph.replace(c, " ")

        p = list(paragraph.lower().split())  # make all character lower case and splite with space
        count = collections.Counter(p)  # put this list into counter.

        ans, most = '', 0
        for word in count:  # for every word in count
            if count[word] > most and word not in banset:  # if the counter is max and not in banset, return it.
                ans, most = word, count[word]

        return ans