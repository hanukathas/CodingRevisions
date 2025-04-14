from trees.tree_node import TreeNode


def binary_tree_tile(root: TreeNode):
    """
    tilt of a tree is the absolute difference of left and right subtrees
    for a given subtree with a single left and right subtree, the tilt is the difference
    this is a bottom up solution
    :param head:
    :return:
    """
    if not root:
        return 0

    binary_tree_tile_result = list()

    def binary_tree_tile_helper(leaf: TreeNode):
        if leaf.left is None and leaf.right is None:
            return leaf.val
        left_sum = right_sum = 0
        if leaf.left is not None:
            left_sum = binary_tree_tile_helper(leaf.left)
        if leaf.right is not None:
            right_sum = binary_tree_tile_helper(leaf.right)
        tilt = abs(left_sum - right_sum)
        binary_tree_tile_result.append(tilt)
        return leaf.val + left_sum + right_sum

    binary_tree_tile_helper(root)
    return binary_tree_tile_result


