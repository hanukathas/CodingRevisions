from collections import deque

from trees.tree_node import TreeNode


def zigzag_level_order(root: TreeNode):
    if not root:
        return None
    queue = deque()
    queue.append(root)
    result = []
    ltor = True
    while len(queue) > 0:
        level_elements = []
        n = len(queue)
        for _ in range(len(queue)):
            leaf = queue.popleft()
            level_elements.append(leaf.val)
            if leaf.left:
                queue.append(leaf.left)
            if leaf.right:
                queue.append(leaf.right)
        if not ltor:
            level_elements = reversed(level_elements)
        result.append(level_elements)
        ltor = not ltor
    return result
