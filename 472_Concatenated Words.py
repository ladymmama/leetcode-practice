class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word,initial,memo):
            if word in memo:                        #if word in memory,return it's value
                return memo[word]
            if word in wordDict and not initial:    # if the word is in worddict and not the first and not from the origin string.
                memo[word]= 1
                return True
            for i in range(1,len(word)):
                if word[:i] in wordDict and dfs(word[i:],False,memo): # if the left parts in dict and the result for dfs the right part are both true
                    memo[word]=1                                      # the whole parts is True.
                    return True
            memo[word]=0                                              # otherwise, its false
            return False

        wordDict=set(words)                                           # remove duplicate
        ans=[]
        for word in words:                                            # dfs every item in words, if its true, we append this value.
            if dfs(word,True,{}):
                ans.append(word)
        return ans