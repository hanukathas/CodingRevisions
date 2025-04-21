class TrieNode:
    def __init__(self, end = False):
        self.children = {}
        self.is_end = end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, node: TrieNode, word: str):
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            curr.children[letter] = TrieNode()
        curr.is_end = True

    def search(self, word: str):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.is_end ## if a word ends here then this word ends here

    def starts_with(self, prefix: str):
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True

    






