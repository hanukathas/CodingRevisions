from collections import deque


class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def create_test_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def level_order_traversal(root: TreeNode):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        cur_level = len(queue)
        cur_level_elements = []
        for _ in range(cur_level):
            leaf = queue.popleft()
            cur_level_elements.append(leaf.val)
            if leaf.left:
                queue.append(leaf.left)
            if leaf.right:
                queue.append(leaf.right)
        result.append(cur_level_elements)
    return result


if __name__ == '__main__':
    test_tree = create_test_tree()
    result = level_order_traversal(test_tree)
    print(result)

