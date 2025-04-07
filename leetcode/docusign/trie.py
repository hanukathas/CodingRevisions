from collections import deque
from dataclasses import field


class Trie:
    def __init__(self):
        self.trie = list()

    def insert(self, word:str):
        if word not in self.trie:
            self.trie.append(word)
            return True
        else:
            return False

    def search(self, word: str):
        if word not in self.trie:
            return False
        return True

    def starts_with(self, prefix: str) -> bool:
        length = len(prefix)
        for word in self.trie:
            if prefix in word[:length]:
                return True

        return False

if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.insert("aple"))
    print(trie.search("apple"))
    print(trie.starts_with("ap"))
    print(trie.starts_with("app"))
    print(trie.starts_with("ba"))
