from typing import AnyStr
from trees.tree_node import TreeNode


def search_tree(head: TreeNode, val):
    if not head:
        return False

    curr = head
    while curr:
        if val == curr.val:
            return True
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    return False