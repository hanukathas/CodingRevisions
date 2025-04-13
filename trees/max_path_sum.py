from trees.tree_node import TreeNode


def max_path_sum(root: TreeNode):
    """
        1. max sum at a leaf level, is the leaf val, or leaf val + left sum or leaf val + right sum, or leaf.val + left sum + right sum
        2.
    :param root:
    :return:
    """
    if not root:
        return 0

    max_path_sum_result = list()
    def max_path_sum_helper(leaf: TreeNode):
        max_sum = leaf.val
        if leaf.left is None and leaf.right is None:
            pass # leaf node, not much to be done

        max_left_sum = max_right_sum = max_sum
        if leaf.left is not None:
            max_left_sum = max_path_sum_helper(leaf.left)
        if leaf.right is not None:
            max_right_sum = max_path_sum_helper(leaf.right)
        max_local_sum = max(max_sum, max_left_sum + max_sum, max_right_sum + max_sum, max_right_sum + max_sum + max_right_sum)
        max_sum = max(max_sum, max_sum + max_left_sum, max_sum + max_right_sum)

        max_path_sum_result[0] = max(max_path_sum_result[0], max_local_sum)
        return max_sum

    max_path_sum_helper(root)
    return max_path_sum_result