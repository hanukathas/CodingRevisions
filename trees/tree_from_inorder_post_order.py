from trees.tree_node import TreeNode


def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    # Build right subtree first because postorder is left-right-root
    root.right = buildTree(inorder[idx+1:], postorder)
    root.left = buildTree(inorder[:idx], postorder)
    return root