class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = "*"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
                curr = curr[letter]
            else:
                curr = curr[letter]
        curr[self.end] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            else:
                curr = curr[letter]

        return self.end in curr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            else:
                curr = curr[letter]

        return True
