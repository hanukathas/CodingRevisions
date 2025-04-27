from trees.tree_node import TreeNode


def check_if_symmetric(root: TreeNode):
    """
    https://leetcode.com/problems/symmetric-tree/description/
    :param root:
    :return:
    """
    def is_mirror(root_1: TreeNode, root_2: TreeNode):
        if root_1 is None and root_2 is None:
            return True
        if root_1 is None or root_2 is None:
            return False
        if root_1.val == root_2.val:
            return is_mirror(root_1.left, root_2.right) and is_mirror(root_1.right, root_2.left)
        return False
    is_mirror(root, root)

def is_symmetric(root: TreeNode):
    def check_symmetry(root1: TreeNode, root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val == root2.val:
            return check_symmetry(root1.left, root2.right) and check_symmetry(root1.right, root2.left)

    return check_symmetry(root.left, root.right)


