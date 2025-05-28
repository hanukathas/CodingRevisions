from trees.tree_node import TreeNode

def valid_bst_recursive(root: TreeNode):
    if root is None:
        return True

    min_val = float('-inf')
    max_val = float('inf')

    def valid_bst_recursive_helper(leaf: TreeNode, min_val: float, max_val:float):
        if leaf is None:
            return True
        if leaf.val < min_val or leaf.val > max_val:
            return False
        return valid_bst_recursive_helper(leaf.left, min_val, leaf.val) and valid_bst_recursive_helper(leaf.right, leaf.val, max_val)
    return valid_bst_recursive_helper(root, min_val, max_val)
