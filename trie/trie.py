class TrieNode:
    def __init__(self, ):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_end = True


    def search(self, word: str):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                print(f"letter: {letter} not there")
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

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print(trie.search("apple"))
    print(trie.search("app"))  # Output: True
    print(trie.search("banana"))  # Output: False
    print(trie.starts_with("ap"))  # Output: True
    print(trie.starts_with("ba"))






