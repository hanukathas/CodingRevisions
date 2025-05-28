from trees.tree_node import TreeNode

def path(root: TreeNode, target: int) -> list:
    """
    Find all paths in the binary tree that sum to the target value.
    :param root: The root of the binary tree.
    :param target: The target sum for the paths.
    :return: A list of lists, where each inner list represents a path that sums to the target.
    """
    global result
    result = []
    path_sum_2(root, target, [])
    return result

def path_sum_2(node: TreeNode, target: int, path: list):
    if node is None:
        return
    path.append(node.val)
    if node.left is None and node.right is None and node.val == target:
        result.append(path[:])
    else:
        path_sum_2(node.left, target - node.val, path)
        path_sum_2(node.right, target - node.val, path)
    path.pop()