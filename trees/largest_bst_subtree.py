from trees.tree_node import TreeNode


def largest_bst_subtree(root: TreeNode):
    """
    1. a leaf is a BST if it has left and right leaves
    2. is this is true: left leaf value < leaf value < right leaf value
    3. if 1 and 2 are true then size = size + 1
    4. set the size to 1, is bst = true, smallest and largest to leaf value
    :param root:
    :return:
    """
    if not root:
        return 1

    largest_bst_subtree_result = list()
    largest_bst_subtree_result[0] = 1
    def largest_bst_subtree_helper(leaf: TreeNode):
        my_size = 1
        is_bst = True
        smallest = largest = leaf.val
        if leaf.right is None and leaf.left is None:
            pass # leaves don't matter
        if leaf.left is not None:
            size, bst, s, l = largest_bst_subtree_helper(leaf.left)
            my_size += size
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not bst or l > leaf.val:
                is_bst = False
        if leaf.right is not None:
            size, bst, s, l = largest_bst_subtree_helper(leaf.right)
            my_size += size
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not bst or s < leaf.val:
                is_bst = False
        if is_bst and my_size > largest_bst_subtree_result[0]:
            largest_bst_subtree_result[0] = my_size
        return my_size, is_bst, smallest, largest

    largest_bst_subtree_helper(root)
    return largest_bst_subtree_result[0]
