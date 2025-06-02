from trees.tree_node import TreeNode

# working solution do not use the bottom ones
def invert_tree(root: TreeNode):
    """
        Inverts (mirrors) a binary tree by recursively swapping the left and right children of every node.

        Given the root of a binary tree, invert the tree and return its root.
        For each node, its left and right children are swapped.

        Example:
            Input:      4
                      /   \
                     2     7
                    / \   / \
                   1   3 6   9

            Output:     4
                      /   \
                     7     2
                    / \   / \
                   9   6 3   1

        :param root: TreeNode, the root of the binary tree
        :return: TreeNode, the root of the inverted binary tree
        """

    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root=root.left)
    invert_tree(root=root.right)

    return root

