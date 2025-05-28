from unittest.mock import right

from trees.tree_node import TreeNode


def balanced_tree(root: TreeNode):
    """
        if the height between root and its children is 1. Means, every level,
        there is a left and right child

        leetcode: https://leetcode.com/problems/balanced-binary-tree/description/
    :param root:
    :return:
    """
    if not root:
        return root

    balanced_tree_result = list()

    def balanced_tree_helper(leaf: TreeNode):
        height = 0
        is_balanced = True
        if leaf.left is None and leaf.right is None:
            pass
        left_height = 0
        right_height = 0
        if leaf.left is not None:
            left_height = 1 + balanced_tree_helper(leaf.left)
        if leaf.right is not None:
            right_height = 1 + balanced_tree_helper(leaf.right)
        if abs(left_height - right_height) > 1:
            is_balanced = False

        balanced_tree_result[0] = is_balanced
        return max(left_height, right_height)

    balanced_tree_helper(root)

    return balanced_tree_result[0]


def is_balanced_tree(leaf: TreeNode, result: bool):
    left_height = 0
    right_height = 0
    if leaf.left is not None:
        left_height = 1 + is_balanced_tree(leaf.left, result)
    if leaf.right is not None:
        right_height = 1 + is_balanced_tree(leaf.right, result)
    if abs(right_height - left_height) > 1:
        result = False
    return abs(right_height - left_height)

def is_balanced_works(root: TreeNode):
    if not root:
        return True
    result = [True]
    def helper(leaf: TreeNode):
        left_height = 0
        right_height = 0
        left_height = helper(leaf.left)

        right_height = helper(leaf.right)

        if abs(left_height - right_height) > 1:
            result = [False]

        return max(left_height, right_height) + 1
        # return this to go up;
        # +1 for the height above this
    helper(root)
    return result

def is_balanced_tree_r(root: TreeNode):
    if not root:
        return None

    def is_balanced_leaf(leaf: TreeNode):
        if leaf.left is None and leaf.right is None:
            pass
        left_level, right_level  = 0, 0
        if leaf.left is not None:
            left_level = is_balanced_leaf(leaf.left)
            if left_level > 1: return -1
        if leaf.right is not None:
            right_level = is_balanced_leaf(leaf.right)
            if right_level > 1: return -1
        if abs(left_level - right_level) > 1:
            return -1
        return max(left_level, right_level) + 1



    return is_balanced_leaf(root) != -1

