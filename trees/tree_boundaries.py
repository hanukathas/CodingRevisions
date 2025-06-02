from trees.tree_node import TreeNode

def tree_boundaries(root: TreeNode):
    if root is None:
        return []

    def is_leaf(node):
        return node.left is None and node.right is None

    left_boundary = []
    curr = root.left
    while curr:
        if not is_leaf(curr):
            left_boundary.append(curr.val)
        curr = curr.left if curr.left else curr.right

    right_boundary = []
    curr = root.right
    while curr:
        if not is_leaf(curr):
            right_boundary.append(curr.val)
        curr = curr.right if curr.right else curr.left

    leaves = []
    def dfs(node):
        if node is None:
            return
        if is_leaf(node):
            leaves.append(node.val)
        else:
            dfs(node.left)
            dfs(node.right)
    dfs(root)

    return [root.val] + left_boundary + [v for v in leaves if v not in left_boundary and v not in right_boundary] + right_boundary[::-1]