class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode):
    def height(node):
        if not root:
            return 0

        left_balanced = height(node.left)
        if left_balanced == -1:
            return -1

        right_balanced = height(node.left)
        if right_balanced == -1:
            return -1

        if abs(left_balanced - right_balanced) > 1:
            return -1

        return max(left_balanced, right_balanced) + 1
    return height(root) != -1






def create_test_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

if __name__ == '__main__':
    test_tree = create_test_tree()
    result = is_balanced(test_tree)
    print(f"Is tree balanced? {result}")