class SimpleTrie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["$"] = {"$"}

    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        if list(curr.keys())[0] == "$":
            return True

    def prefix(self, prefix_word):
        curr = self.root
        for letter in prefix_word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True



