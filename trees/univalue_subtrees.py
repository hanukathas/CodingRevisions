from trees.tree_node import TreeNode


def univalue_subtrees(root: TreeNode):
    if not root:
        return 0
    final_count = 0

    def subtrees(node: TreeNode):
        if node.right is None and node.left is None:
            final_count += 1
            return True
        is_uni_value = True
        if node.left is not None:
            left_is_uni_value = subtrees(node.left)
            if not left_is_uni_value or node.val != node.left.val:
                is_uni_value = False
        if node.right is not None:
            right_is_uni_value = subtrees(node.right)
            if not right_is_uni_value or node.val != node.right.val:
                is_uni_value = False
        if is_uni_value:
            final_count += 1
        return is_uni_value

    subtrees(root)
    return final_count
