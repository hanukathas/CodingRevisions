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

    result = [0]

    def calculate_largest(leaf: TreeNode):
        is_bst = True
        size = 1

        l_size, l_min, l_max, l_bst = calculate_largest(leaf.left)
        r_size, r_min, r_max, r_bst = calculate_largest(leaf.right)

        if l_bst and r_bst and l_max < leaf.val < r_min:
            return (size + l_size + r_size
                        , min(l_min, leaf.val)
                        , max(r_max, leaf.val)
                        , True)
        else:
            return max(l_size, r_size) + 1, 0, 0, False


    size, _, _, bst = calculate_largest(root)
    if bst:
        return size
    return -1








