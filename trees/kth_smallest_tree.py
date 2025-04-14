from trees.tree_node import TreeNode


def kth_smallest_tree(root: TreeNode, k: int):
    """
    1. solve this using in order traversal
    2. when you are a leaf, check if your traversal has reached k.
    3. if you have reached traversal depth of k, and since it's a BST, return the element
    :param root:
    :return:
    """
    # tree is valid, so root is valid
    kth_smallest_tree_result = list()
    def kth_smallest_tree_helper(leaf: TreeNode, height: int):
        # in-order traversal of a BST, results in a sorted list
        # this is an in-order traversal as it's a BST
        # at the leaf node, check if height is reached, else you have hit a leaf node
        if height >= k:
            return height
        if leaf.left is None and leaf.right is None:
            height += 1
            if height == k:
                kth_smallest_tree_result[0] = leaf.val
                return height
        if leaf.left is not None:
            height = kth_smallest_tree_helper(leaf.left, height)
        height += 1
        if height == k:
            kth_smallest_tree_result[0] = height
        if leaf.right is not None:
            height = kth_smallest_tree_helper(leaf.right, height)
        return height

    kth_smallest_tree_helper(root, 0)
    return kth_smallest_tree_result[0]