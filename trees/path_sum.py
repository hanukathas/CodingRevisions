from trees.tree_node import TreeNode

result = list()
def path_sum(node: TreeNode, target: int):
    if node.left is None and node.right is None and node.val == target:
        return True
    if node.left is not None:
        if node.val > target:
            return False
        else:
            return node.left, target - node.val  # what if the values are negative?
    if node.right is not None:
        if node.val > target:
            return False
        else:
            return path_sum(node.right, target - node.val)  # what if the values are negative?

def path_sum_2(node: TreeNode, target: int, path: list):
    if node.left is None and node.right is None and node.val == target:
        path.append(target)
        result.append(path[:])
        path.pop()
        return
    path.append(target - node.val) # allowing for negative values
    if node.right is not None:
        path_sum_2(node.right, target - node.val, path)
    if node.left is not None:
        path_sum_2(node.left, target - node.val, path)
    path.pop()

def dfs(root: TreeNode, target: int):

    if root is None or target == 0: #ask the interviewer what should be returned
        return False
    if root.val == target and root.left is not None and root.right is not None:
        return False
    if root.val == target and root.left is None and root.right is None:
        return True
    if root.val > target:
        return False
    if root.left is not None and root.right is not None and root.val < target:
        path_sum(root.left, target - root.val)
        path_sum_2(root.left, target - root.val, [])
        path_sum(root.right, target - root.val)
        path_sum_2(root.right, target - root.val, [])
    if root.left is not None and root.val < target:
        path_sum(root.left, target - root.val)
        path_sum_2(root.left, target - root.val, [])
    if root.right is not None and root.val < target:
        path_sum(root.right, target - root.val)
        path_sum_2(root.right, target - root.val, [])






