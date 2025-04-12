from leetcode.blackline.level_order_traversal import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode):
    found = [None]
    def helper(leaf: TreeNode):
        pfound = qfound = False
        if leaf == p:
            pfound = True
        if leaf == q:
            qfound = True
        if leaf.right is None and leaf.left is None:
            pass
        if leaf.left is not None:
            pf,qf = helper(leaf.left)
            pfound = pf or pfound
            qfound = qf or qfound
        if pfound and qfound and found[0] is None:
            found[0] = leaf
        return pfound, qfound

    helper(root)
    return found