from sys import prefix


class RTrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class RTrie:
    def __init__(self):
        self.root = RTrieNode()
    def insert(self, word: str):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = RTrieNode()
            curr = curr.children[char]
        curr.is_end = True
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
if __name__ == '__main__':
    trie = RTrie()
    trie.insert("apple")
    trie.insert("app")

    print(trie.search("apple"))  # Output: True
    print(trie.search("app"))  # Output: True
    print(trie.search("banana"))  # Output: False
    print(trie.starts_with("ap"))  # Output: True
    print(trie.starts_with("ba"))
