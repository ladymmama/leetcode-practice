import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        freqList = collections.Counter(words)  # create a dict like: {a:6, b:3}
        heapList = []  # create a heap list to store the heap.
        for s in freqList.keys():  # every words in the string
            heapq.heappush(heapList, [-freqList[s], s])  # we push the [-freqList[s], s] into our heaplist

        return [heapq.heappop(heapList)[1] for _ in range(k)]  # output the first k th :"s"