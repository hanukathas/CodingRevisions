from trees.tree_node import TreeNode


def univalue_subtrees(root: TreeNode):
    result = [0]

    def helper(leaf: TreeNode):
        if root is None:
            return True
        if leaf.left is not None:
            is_left_unival = helper(leaf.left)
        if leaf.right is not None:
            is_right_unival = helper(leaf.right)

        is_leaf_unival = True

        if (not leaf.left or (is_left_unival and leaf.value == leaf.left.value)) and (
                not leaf.right or (is_right_unival and leaf.value == leaf.right.value)):
            result[0] += 1
            is_leaf_unival = True
        else:
            is_leaf_unival = False

        return is_leaf_unival

    helper(root)
    return result[0]

