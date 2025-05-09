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

def insert_node_r(head: TreeNode, k: AnyStr):
    """
    we are just inserting at leaf node
    :param head:
    :param k:
    :return:
    """
    prev = None
    leaf = TreeNode(val=k)
    curr = head
    while curr:
        if curr.val == leaf.val:
            return head
        if curr.val < leaf.val:
            prev = curr
            curr = curr.right
        if curr.val > leaf.val:
            prev = curr
            curr = curr.left

    if prev.val < leaf.val:
        prev.right = leaf
        leaf.left = prev
    else:
        prev.left = leaf
        leaf.right = prev




