from trees.tree_node import TreeNode


def in_order(leaf: TreeNode, results: []):

    if leaf.left is not None:
        in_order(leaf.left, results)
    results.append(leaf.val)
    if leaf.right is not None:
        in_order(leaf.right, results)

    return  results


def pre_order(leaf: TreeNode, results:[]):
    results.append(leaf.val)
    if leaf.left is not None:
        in_order(leaf.left, results)
    if leaf.right is not None:
        in_order(leaf.right, results)

    return results


def post_order(leaf: TreeNode, results: []):

    if leaf.left is not None:
        in_order(leaf.left, results)
    if leaf.right is not None:
        in_order(leaf.right, results)
    results.append(leaf.val)
    return results


def dfs():
    root = TreeNode(val=0)
    results = []
    print(in_order(root, results))
    print(pre_order(root, results))
    print(post_order(root, results))


