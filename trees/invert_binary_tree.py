from trees.tree_node import TreeNode

# working solution do not use the bottom ones
def invert_tree(root: TreeNode):
    """
    working solution
    :param root:
    :return:
    """
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root=root.left)
    invert_tree(root=root.right)

    return root

