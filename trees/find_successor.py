from contextlib import nullcontext

from company_specific.blackline.level_order_traversal import TreeNode


def find_successor(node: TreeNode, root: TreeNode):
    """
    https://leetcode.com/problems/inorder-successor-in-bst/description/
    :param node:
    :param root:
    :return:
    """
    if not root:
        return None
    if node.right:
        curr = node.right
        while curr:
            curr = curr.left
        return curr
    parent = None
    curr = root
    while curr != node:
        if curr.val < node.val:
            parent = curr
            curr = curr.left
        else:
            curr = curr.right
    return parent
def find_successor_revision(node: TreeNode, root: TreeNode):
    if not root or node is None:
        return None
    if node.right:
        successor = node.right
        while successor:
            successor = successor.left
            if successor.left is None:
                return successor.val
    else:
        ancestor = None
        curr = root
        while curr:
            if curr.val < node.val:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right
        return ancestor

def working_solution(p: TreeNode, root: TreeNode):
    if p.right:
        curr = p.right
        while curr:
            if curr.left is None:
                return curr
            curr = curr.left

    curr = root
    ancestor = None
    while curr:
        if p.val < curr.val:
            ancestor = curr
            curr = curr.left
        else:
            curr = curr.right
    return ancestor


