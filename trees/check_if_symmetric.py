from trees.tree_node import TreeNode


def check_if_symmetric(root: TreeNode):
    def is_mirror(root_1: TreeNode, root_2: TreeNode):
        if root_1 is None and root_1 is None:
            return True
        if root_1 is None or root_2 is None:
            return False
        if root_1.val == root_2.val:
            return is_mirror(root_1.left, root_2.right) and is_mirror(root_1.right, root_2.left)
        return False



    is_mirror(root, root)
