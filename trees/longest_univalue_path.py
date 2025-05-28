from trees.tree_node import TreeNode

def longest_uni_value_path(root: TreeNode):
    """
    Returns the length of the longest path where all nodes have the same value.
    The path may or may not pass through the root.
    """
    if not root:
        return 0  # An empty tree has path length 0

    result = [0]  # Mutable container to store the global maximum path length

    def helper(node):
        if not node:
            return 0  # Base case: no path from a null node

        # Recursively get the longest univalue path for left and right children
        left = helper(node.left)
        right = helper(node.right)

        left_path = right_path = 0  # Paths starting from this node

        # If left child exists and has the same value, extend the left path
        if node.left and node.left.val == node.val:
            left_path = left + 1

        # If right child exists and has the same value, extend the right path
        if node.right and node.right.val == node.val:
            right_path = right + 1

        # Update the global result: the longest path through this node
        result[0] = max(result[0], left_path + right_path)

        # Return the longest single path (either left or right) to parent
        return max(left_path, right_path)

    helper(root)
    return result[0]

def uni_value_tree(root: TreeNode):
    if not root:
        return True

    max_size = [0]
    def helper(leaf: TreeNode):
        if not leaf:
            return 0

        left_size = helper(leaf.left)
        right_size = helper(leaf.right)


    return max_size

if __name__ == "__main__":
    # Example usage:
    # Constructing a tree:
    #       5
    #      / \
    #     4   5
    #    / \
    #   1   1
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)

    print(longest_uni_value_path(root))  # Output: 2 (the path 4 -> 5 or 5 -> 5)