from trees.tree_node import TreeNode


def tree_from_inorder_preorder(in_order: list, pre_order: list):
    if len(in_order) == 0 or len(pre_order) == 0:
        return TreeNode(val=None)
    hmap = {}
    for i in range(len(in_order)):
        hmap[in_order[i]] = i


    def helper(P, startP, endP, I, startI, endI):
        if startP > endP:
            return TreeNode(val=None)
        if startI == endI:
            return TreeNode(val=P[0])
        root = TreeNode(val=P[0])
        root_index = hmap[P[0]]
        nums_left = root_index - startI
        root.left = helper(P, startP+1, startP + nums_left, I, startI, root_index)
        root.right = helper(P, startP+nums_left+1, endP, I, root_index+1, endI)
        return root

    return helper(pre_order, 0, len(pre_order), in_order, 0, len(in_order))




