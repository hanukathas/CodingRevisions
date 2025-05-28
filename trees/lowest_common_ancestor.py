from leetcode.blackline.level_order_traversal import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right

def lca_r(root: TreeNode, p: TreeNode, q: TreeNode):
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
    :param root:
    :param p:
    :param q:
    :return:
    """
    if not root or root == p or root == q:
        return root

    left = lca_r(root.left, p, q)
    right = lca_r(root.right, p, q)

    if left and right:
        return root

    return left if left else right
