from trees.tree_node import TreeNode


def invert_binary_tree(root: TreeNode):
    if not root:
        return root
    def inverter(leaf: TreeNode):
        if leaf.left is not None and leaf.right is not None:
            left = leaf.left
            right = leaf.right
            leaf.right = left
            leaf.left = right
        if leaf.left is  None and leaf.right is  None:
            pass
        if leaf.left is  None and leaf.right is not None:
            right = leaf.right
            leaf.left = right
        if leaf.left is not None and leaf.right is  None:
            left = leaf.left
            leaf.right = left


    inverter(root)
    return root

def invert_binary_tree_r(root: TreeNode):
    if not root:
        return None
    def inverter_r(leaf: TreeNode):
        if leaf.left is not None and leaf.right is not None:
            left = leaf.left
            right = leaf.right
            leaf.right = left
            leaf.left = right
        if leaf.left is None and leaf.right is not None:
            right = leaf.right
            leaf.left = right
            leaf.right = None
        if leaf.left is not None and leaf.right is  None:
            left = leaf.left
            leaf.right = left
            leaf.left = None
    inverter_r(root)
    return root