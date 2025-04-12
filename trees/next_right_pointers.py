from collections import deque


class NextTreeNode:
    def __int__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def next_right_pointers(root: NextTreeNode):
    if not root:
        return None

    queue = deque()
    queue.append(root)

    while len(queue):
        n = len(queue)
        prev = NextTreeNode()

        for _ in range(len(queue)):

            leaf = queue.popleft()
            if prev is None:
                prev = leaf
            else:
                prev.next = leaf

            if leaf.left is not None:
                queue.append(leaf.left)
            if leaf.right is not None:
                queue.append(leaf.right)
    return root







