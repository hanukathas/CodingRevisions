from trees.tree_node import TreeNode


def largest_bst_subtree(root: TreeNode):
    """
    https://leetcode.com/problems/largest-bst-subtree/
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


def largest_bst_subtree_r_works(root: TreeNode):
    """
    https://leetcode.com/problems/largest-bst-subtree/
    top - bottom traversal
    :param root:
    :return:
    """
    if not root:
        return root

    largest_st = [1]
    def get_largest(leaf: TreeNode):
        size = 1 # one more lower level
        smallest = leaf.val
        largest = leaf.val
        is_bst = True

        if leaf.left is None and leaf.right is None:
            pass
        if leaf.left is not None:
            left_size, s, l, bst = get_largest(leaf.left)
            smallest = min(smallest, s)
            largest = max(largest, l)
            size += left_size
            if not bst or l > leaf.val:
                is_bst = False
        if leaf.right is not None:
            right_size, s, l, bst = get_largest(leaf.right)
            smallest = min(smallest, s)
            largest = max(largest, l)
            size += right_size
            if not bst or s < leaf.val:
                is_bst = False
            if size > largest_st[0]:
                largest_st[0] = size
            return size, smallest, largest, is_bst

    get_largest(root)
    return largest_st