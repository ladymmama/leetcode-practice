class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = collections.Counter(secret)
        bulls = 0
        cows = 0

        # First loop is going to count the Bulls, so same digits sharing the same position
        # Also if True decrement the count for respective number
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                d[secret[i]] -= 1

        # Secoud loop is going to count the cows, numbers that are not same is the dictionary
        # with counts greater than zero
        # Also decrement the respective number if True
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in d and d[guess[i]] > 0:
                cows += 1
                d[guess[i]] -= 1

        return str(bulls) + "A" + str(cows) + "B"


