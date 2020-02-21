class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        if not s or not s[0]:
            return 0
        stack = []              #create a stack to pair
        stack.append(-1)        #index start from 0, push -1, so when using index - peek, we can get the right length
        count = 0
        for i in range(len(s)):
            if s[i] == "(":     #everytime, we have a (, we push into the stack
                stack.append(i)
            elif s[i] == ")":    #if we met a ), we can pop it
                stack.pop()
                if (len(stack) == 0):   #if there is no ( before, so the stack will be empty
                    stack.append(i)     #at this time we have to push this index again as we push -1 at the first
                else:                   #everytime we pop we compare the length to find the max length
                    count = max(count, i-stack[-1])
        return count