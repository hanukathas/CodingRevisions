from trees.tree_node import TreeNode


def buildTree(inorder: list, postorder: list) -> TreeNode:
    if not inorder or not postorder:
        return None

    # Create hash map for O(1) lookup
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(in_start: int, in_end: int, post_start: int, post_end: int) -> TreeNode:
        if in_start > in_end:
            return None

        root = TreeNode(postorder[post_end])
        root_idx = inorder_map[postorder[post_end]]
        left_size = root_idx - in_start

        root.left = helper(in_start, root_idx - 1,
                           post_start, post_start + left_size - 1)
        root.right = helper(root_idx + 1, in_end,
                            post_start + left_size, post_end - 1)

        return root

    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)