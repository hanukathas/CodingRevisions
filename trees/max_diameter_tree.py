from trees.tree_node import TreeNode


def max_diameter_tree(root: TreeNode):
    if not root:
        return []
    result = [0]

    def helper(node: TreeNode):
        if node.right is None and node.left is None:
            return 0
        diameter = 0
        left_diameter = right_diameter = 0
        if node.left is not None:
            left_diameter = helper(node.left)
            diameter += left_diameter + 1
        if node.right is not None:
            right_diameter = helper(node.right)
            diameter += right_diameter + 1
        result[0] = max(result[0], diameter)
        return max(left_diameter, right_diameter) + 1


    helper(root)
    return result

def max_diameter_r(root: TreeNode):
    """
    https://leetcode.com/problems/diameter-of-binary-tree/description/
    :param root:
    :return:
    """
    if not root:
        return 0

    max_d = [0]
    def diameter_calculator(leaf: TreeNode):
        diameter = 0
        left_diameter = 0
        right_diameter = 0
        if leaf.left is not None:
            left_diameter = diameter_calculator(leaf.left)
            diameter = 1 + left_diameter
        if leaf.right is not None:
            right_diameter = diameter_calculator(leaf.right)
            diameter += 1 + right_diameter
        max_d[0] = max(max_d[0], diameter)
        return max(left_diameter, right_diameter) + 1 # add 1 for self diameter
    diameter_calculator(root)
    return max_d
