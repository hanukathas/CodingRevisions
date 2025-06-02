from trees.tree_node import TreeNode


def balanced_tree(root: TreeNode):
    """
        if the height between root and its children is 1. Means, every level,
        there is a left and right child

        company_specific: https://leetcode.com/problems/balanced-binary-tree/description/
    :param root:
    :return:
    """
    if not root:
        return root
    def is_balanced_tree(leaf: TreeNode):
        left_size, right_size = 0, 0
        if leaf is None:
            return 0
        left_size = is_balanced_tree(leaf.left)
        right_size = is_balanced_tree(leaf.right)

        if left_size == -1:
            return -1
        elif right_size == -1:
            return -1
        elif abs(left_size - right_size) > 1:
            return -1
        else:
            return max(left_size, right_size) + 1

    return is_balanced_tree(root) != -1




def is_balanced_tree_r(root: TreeNode):
    if not root:
        return None

    def is_balanced_leaf(leaf: TreeNode):
        if leaf.left is None and leaf.right is None:
            pass
        left_level, right_level  = 0, 0
        if leaf.left is not None:
            left_level = is_balanced_leaf(leaf.left)
            if left_level == -1 : return -1
        if leaf.right is not None:
            right_level = is_balanced_leaf(leaf.right)
            if right_level == -1: return -1
        if abs(left_level - right_level) > 1:
            return -1
        return max(left_level, right_level) + 1



    return is_balanced_leaf(root) != -1

