from typing import List


class TrieNode:
    def __init__(self):
        # children[0] is for '0', children[1] is for '1'
        self.children = [None, None]
        # last stores the most recent command index passing here
        self.last = -1

def autocomplete(commands: List[str]) -> List[int]:
    # Initialize the Trie root and the answer list
    root = TrieNode()
    result: List[int] = []

    # Process each command in order
    for j, cmd in enumerate(commands):
        if j == 0:
            # First command has no previous commands
            result.append(0)
        else:
            node = root
            best_idx = -1
            matched = False
            # Search for the longest prefix in the Trie
            for ch in cmd:
                bit = 0 if ch == '0' else 1
                # If the child exists, we can extend the prefix
                if node.children[bit]:
                    node = node.children[bit]
                    matched = True
                    # node.last is the most recent command with this prefix
                    best_idx = node.last
                else:
                    break
            # If we matched at least one character, use best_idx
            # Otherwise fall back to the immediately previous command
            result.append(best_idx if matched else j - 1)

        # Insert/update the full command into the Trie
        node = root
        for ch in cmd:
            bit = 0 if ch == '0' else 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            # mark this node with the current command index
            node.last = j

    return result

if __name__ == '__main__':
    command = ['0000', '1111', '010', '11', '11100']
    print(autocomplete(command))