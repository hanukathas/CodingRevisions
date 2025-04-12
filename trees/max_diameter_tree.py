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
