from trees.tree_node import TreeNode

def dfs(root: TreeNode):
    result = []
    if not root:
        return None
    dfs_pre_order(root, result)
    dfs_in_order(root, result)
    dfs_post_order(root, result)

def dfs_pre_order(root: TreeNode, result: list):
    if not root:
        return None
    result.append(root.val)
    dfs_pre_order(root.left, result)
    dfs_pre_order(root.right, result)

def dfs_in_order(root: TreeNode, result: list):
    if not root:
        return None

    dfs_in_order(root.left, result)
    result.append(root.val)
    dfs_in_order(root.right, result)


def dfs_post_order(root: TreeNode, result: list):
    if not root:
        return None

    dfs_post_order(root.left, result)
    dfs_post_order(root.right, result)
    result.append(root.val)

