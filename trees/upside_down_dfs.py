from collections import deque

from trees.tree_node import TreeNode


def upside_down_dfs(root: TreeNode):
    if not root:
        return None
    global_root = list()
    def upside_down_dfs_helper(leaf: TreeNode, parent: TreeNode, righ_leaf: TreeNode):
        if leaf.left is None and leaf.right is None:
            global_root[0] = leaf

        old_left = leaf.left
        old_right = leaf.right
        leaf.left = righ_leaf
        leaf.right = parent

        if old_left is not None:
            upside_down_dfs_helper(old_left, leaf, old_right)
    # here we send the root, and then the subsequent recursions will handle the rotation
    upside_down_dfs_helper(root, None, None)
    return global_root[0]

def upside_down_bfs(root: TreeNode):
    if not root:
        return None
    queue = deque()
    queue.append([(root, None, None)])
    upside_down_root = list()
    while len(queue) > 0:
        leaf, parent, right_sibling = queue.popleft()
        upside_down_root = leaf
        old_left = leaf.left
        old_right = leaf.right
        leaf.left = right_sibling
        leaf.right = parent
        if old_left is not None:
            queue.append([(old_left, leaf, old_right)])
    return upside_down_root






