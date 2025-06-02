from trees.tree_node import TreeNode

def valid_bst(root: TreeNode):
    if not root:
        return True

    min_val = float('-inf')
    max_val = float('inf')

    def bst_validator(leaf, left_val, right_val):
        if leaf is None:
            return True
        if (not left_val <= leaf.val < right_val
                or not left_val < leaf.val <= right_val):
            return False
        return (bst_validator(leaf.left, min_val, leaf.val)
                and bst_validator(leaf.right, leaf.val, max_val))

    return bst_validator(root, min_val, max_val)
