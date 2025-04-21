class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def longestWord(self, words):
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        # DFS to find longest word
        self.longest = ""

        def dfs(node, curr_word):
            if len(curr_word) > len(self.longest) or (len(curr_word) == len(self.longest) and curr_word < self.longest):
                self.longest = curr_word

            for char, child in node.children.items():
                if child.is_word:  # Only traverse if it forms a word
                    dfs(child, curr_word + char)

        dfs(root, "")
        return self.longest


# Example usage
if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world", "worlc"]
    solution = Solution()
    result = solution.longestWord(words)
    print(f"Longest word that can be built one character at a time: {result}")  # Output: world



