from trees.tree_node import TreeNode


def binary_tree_tile(root: TreeNode):
    """
    leet code: https://leetcode.com/problems/binary-tree-tilt/
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

def binary_tree_tile_r(leaf: TreeNode, tile: list):
    left_sum = 0
    right_sum = 0
    if leaf.left is not None:
        left_sum = binary_tree_tile_r(leaf.left, tile)
    if leaf.right is not None:
        right_sum = binary_tree_tile_r(leaf.right, tile)
    tile += abs(left_sum - right_sum)

    return left_sum + right_sum + leaf.val

def binary_tree_tile_r2(leaf: TreeNode, tile: list):
    left_sum = 0
    right_sum = 0
    if leaf.left is not None:
        left_sum = binary_tree_tile_r2(leaf.left, tile)
    if leaf.right is not None:
        right_sum = binary_tree_tile_r2(leaf.right, tile)
    tile.append(abs(right_sum - left_sum))
    return leaf.val + left_sum + right_sum









