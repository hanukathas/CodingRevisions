from collections import deque

from trees.tree_node import TreeNode


def bfs(root: TreeNode):
    if not root:
        return None
    queue = deque()
    elements = []
    curr = root

    queue.append(curr)

    while len(queue) > 0:
        element = queue.popleft()
        elements.append(element.val)
        if element and element.right:
            queue.append(element.right)
        if element and element.left:
            queue.append(element.left)



