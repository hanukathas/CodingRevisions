from trees.tree_node import TreeNode

def upside_down_dfs(root: TreeNode):
    if not root:
        return None

    root_index = [root]

    def build_upside_down(leaf: TreeNode, right_leaf: TreeNode, parent: TreeNode):
        if leaf.left is None and leaf.right is None:
            root_index[0] = leaf
        old_left = leaf.left
        old_right = leaf.right

        leaf.left = right_leaf
        leaf.right = parent

        if old_left:
            build_upside_down(old_left, old_right, leaf)



    build_upside_down(root, None, None)

    return root_index[0]


