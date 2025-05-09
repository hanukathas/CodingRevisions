from trees.tree_node import TreeNode


def serialize_binary_tree(root: TreeNode):
    """
    use pre-order. when a left or right is null then add -1 as val
    :param root:
    :return:
    """
    if not root:
        return root

    serialize_binary_tree_elements = list()
    def serialize_binary_tree_helper(leaf: TreeNode):
        serialize_binary_tree_elements.append(leaf.val)
        if leaf.left is not None:
            serialize_binary_tree_helper(leaf.left)
        else:
            serialize_binary_tree_elements.append(TreeNode(val=-1))
        if leaf.right is not None:
            serialize_binary_tree_helper(leaf.right)
        else:
            serialize_binary_tree_elements.append(TreeNode(val=-1))
    serialize_binary_tree_helper(root)
    return serialize_binary_tree_elements

def serialize_binary_tree_r(root: TreeNode):
    """
    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
    use preorder traversal to generate the tree
    :param root:
    :return:
    """
    if not root:
        return None
    elements = []
    def serializer(leaf: TreeNode):
        if not leaf:
            return -1
        elements.append(leaf.val)
        if leaf.left is not None:
            serializer(leaf.left)
        else:
            elements.append(-1)
        if leaf.right is not None:
            serializer(leaf.right)
        else:
            elements.append(-1)
    serializer(root)
    return elements