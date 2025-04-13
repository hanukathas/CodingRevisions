from trees.tree_node import TreeNode


def tree_boundaries(root: TreeNode):
    """
    understanding the problem is important
    1. construct the left boundary
    2. construct and append the leaves
    3. construct and append the right boundary

    very difficult to do it one loop, do it in 3 loops

    we pop the last node because it's a leaf
    :param root:
    :return:
    """
    if root is None:
        return root

    # get the left boundary first
    left_boundary = [root.val]

    if root.left is not None:
        curr = root.left
        while curr is not None:
            left_boundary.append(curr.val)
            if curr.left is not None:
                curr = curr.left
            else:
                curr = curr.right
        # pop the leaf
        left_boundary.pop()

    right_boundary = []
    if root.right is not None:
        curr = root.right
        while curr is not None:
            right_boundary.append(curr.val)
            if curr.right is not None:
                curr = curr.right
            else:
                curr = curr.right
        right_boundary.pop()  # pop the leaf at the end
    leaves = []
    def helper(leaf: TreeNode):
        if leaf.right is None and leaf.left is None:
            leaves.append(leaf.val)
        if leaf.left is not None:
            helper(leaf.left)
        if leaf.right is not None:
            helper(leaf.right)
    helper(root)

    return left_boundary + leaves + right_boundary


