from contextlib import nullcontext
from wsgiref.validate import header_re

from trees.tree_node import TreeNode


def delete_leaf(root: TreeNode, key: int):
    if not root:
        return None
    prev = None
    curr = root

    while curr:
        if curr.val == key:
            break
        if curr.val < key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    if curr is None:
        return None

    if prev is None:
        return None

    # find if it's a leaf node:
    if curr.left is None and curr.right is None:
        if curr.val < prev.val:
            prev.left = None
            curr = None
        else:
            prev.right = None
            curr = None
    elif curr.left is None and curr.right is not None:
        child = curr.right
        if prev is None:
            return child
        if prev.val < curr.val:
            prev.right = child
        else:
            prev.left = child
    elif curr.left is not None and curr.right is None:
        child = curr.left
        if prev is None:
            return child
        if prev.val < curr.val:
            prev.left = child
        else:
            prev.right = child





