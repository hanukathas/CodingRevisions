from trees.tree_node import TreeNode


def balanced_tree(root: TreeNode):
    """
        if the height between root and its children is 1. Means, every level,
        there is a left and right child
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
