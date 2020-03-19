class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_dict = dict()
        for word in words:
            word_dict[word] = set(word)
        max_len = 0
        for i1, w1 in enumerate(words):
            for i2 in range(i1+1, len(words)):
                w2 = words[i2]
                if not (word_dict[w1] & word_dict[w2]):
                    max_len = max(max_len, len(w1) * len(w2))
        return max_len