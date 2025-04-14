from collections import deque

from leetcode.blackline.level_order_traversal import TreeNode


def deserialize_tree(arr: deque):
    if len(arr) == 0:
        return None # return None for empty array
    def deserialize_tree_helper(queue: deque):
        if len(queue) == 0:
            return None
        q = queue.popleft()
        if q is None:
            return
        else:
            root = TreeNode(val=q)
            root.left = deserialize_tree_helper(queue)
            root.right = deserialize_tree_helper(queue)
            return root

    return deserialize_tree_helper(arr)
