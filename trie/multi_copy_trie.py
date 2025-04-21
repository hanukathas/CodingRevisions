class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        self.total = 0 # needed to keep how many places this letter is being used

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for letter in word:
            curr.total += 1
            if not letter in curr.children:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]

        curr.count += 1

    def starts_with(self, prefix):
        curr = self.root

        for letter in prefix:

            if not letter in curr.children:
                return False
            curr = curr.children[letter]
        return True

    def erase(self, word):
        curr = self.root
        for letter in word:
            curr.total -= 1
            # what if the letters from this child on is 1 ( a single copy), that we have appdex, appdex2 and apple.
            # we are l, if we reduce total at l, we know the trie does  not have any more words. so we can just
            # delete the entry from here
            if curr.total == 1:
                del curr.children[letter]
                curr.count = 0
                return
            curr = curr.children[letter]
        curr.total -= 1
        curr.count -= 1
        if curr.count == 0:
            del curr.children[word[-1]]





