from typing import AnyStr

from trees.tree_node import TreeNode


def insert_node(head: TreeNode, k: AnyStr):
    new_node = TreeNode(val=k)
    if not head:
        return new_node

    curr = head
    prev = None

    while curr:
        if curr.val == new_node.val:
            return head
        if curr.val < new_node.val:
            prev = curr
            curr = curr.right
        if curr.val > new_node.val:
            prev = curr
            curr = curr.left

    if prev.val < new_node.val:
        prev.right = new_node
        new_node.left = prev
    else:
        prev.left = new_node
        new_node.right = prev

    return head