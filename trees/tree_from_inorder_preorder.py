from turtledemo.penrose import start

from trees.tree_node import TreeNode


def tree_from_inorder_preorder(in_order: list, pre_order: list):
    if len(in_order) == 0 or len(pre_order) == 0:
        return TreeNode(val=-1)
    hmap = {} # optimize to get the indexes
    for i in range(len(in_order)):
        hmap[in_order[i]] = i


    def helper(P, startP, endP, I, startI, endI):
        if startP > endP:
            return TreeNode(val=-1)
        if startI == endI: # in order, root will be the only element
            return TreeNode(val=P[0])
        root = TreeNode(val=P[0])
        root_index = hmap[P[0]]
        nums_left = root_index - startI
        root.left = helper(P, startP+1, startP + nums_left, I, startI, root_index)
        root.right = helper(P, startP+nums_left+1, endP, I, root_index+1, endI)
        return root

    return helper(pre_order, 0, len(pre_order), in_order, 0, len(in_order))

def tree_from_inorder_preorder_r(in_order: list, pre_order: list):
    if len(in_order) == 0 or len(pre_order) == 0:
        return TreeNode(val=-1)
    if len(in_order) != len(pre_order):
        return TreeNode(val=-1)
    if len(in_order) == 1:
        return TreeNode(val=in_order[0])

    hmap = {}
    for i in range(len(in_order)):
        hmap[in_order[i]] = i

    p_start_ = 0
    p_end_ = len(pre_order) # no -1 as this is the boundary

    i_start_ = 0
    i_end_ = len(in_order) # no -1 as this is the boundary

    def generate_tree(P: [], p_start: int, p_end: int, I: [], i_start: int, i_end: int):
        if p_end < p_start:
            return TreeNode(val=-1)
        if p_start == p_end:
            return TreeNode(val=P[0])
        i_index = hmap[P[0]]
        length = i_index - p_start
        root = TreeNode(val=P[0])
        root.left = generate_tree(P, p_start, p_start + length, I, i_start, i_index)
        root.right = generate_tree(P, p_start + length + 1, p_end, I, i_index+1, i_end)
        return root
    return generate_tree(P=pre_order, I=in_order, p_start=p_start_, p_end=p_end_, i_start=i_start_, i_end=i_end_)








