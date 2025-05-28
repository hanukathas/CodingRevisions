from trees.tree_node import TreeNode


def largest_bst_subtree_r_works(root: TreeNode):
    """
    https://leetcode.com/problems/largest-bst-subtree/
    top - bottom traversal
    :param root:
    :return:
    """
    if not root:
        return root

    def helper(node):
        if not node:
            return 0, float('inf'), float('-inf'), True  # size, min, max, is_bst

        l_size, l_min, l_max, l_bst = helper(node.left)
        r_size, r_min, r_max, r_bst = helper(node.right)

        if l_bst and r_bst and l_max < node.val < r_min:
            size = l_size + r_size + 1
            return size, min(l_min, node.val), max(r_max, node.val), True
        else:
            return max(l_size, r_size), 0, 0, False
    # Call the helper function and get the size of the largest BST subtree

    size, _, _, _ = helper(root)
    return size

def largest_bst_subtree_r2(root: TreeNode):
    if not root:
        return 0
    def helper(leaf):
        is_bst = True
        size = 1
        l_size, r_size = 0, 0
        l_size, lmin, lmax, lbst = helper(leaf.left)
        r_size, rmin, rmax, rbst = helper(leaf.right)

        if lbst and rbst and lmax < leaf.val < rmin:
            is_bst = True
            size = size + l_size + r_size
            return size, min(lmin, leaf.val), max(rmax, leaf.val), is_bst
        else:
            return max(l_size, r_size), 0, 0, False




