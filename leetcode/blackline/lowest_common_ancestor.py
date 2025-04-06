class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_test_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def lowest_common_ancestor(root: TreeNode, p:TreeNode, q: TreeNode):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root

    return left if left else right


if __name__ == '__main__':
    test_tree = create_test_tree()
    node1 = test_tree.left.right  # node with value 5
    node2 = test_tree.left.left  # node with value 1
    result = lowest_common_ancestor(test_tree, node1, node2)
    print(f"Is tree balanced? {result.val}")