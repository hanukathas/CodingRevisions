import queue
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

def deserialize_tree_r(arr: deque):
    """
    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
    1. go by the order of the elements
    2. whe a value is null or none just return

    :param arr:
    :return:
    """
    if not arr:
        return None

    def dt_helper(arr):
        if len(arr) == 0:
            return None
        val = arr.popleft()
        if not val:
            return None
        root = TreeNode(val)
        root.left = dt_helper(arr)
        root.right = dt_helper(arr)

        return root


    return dt_helper(arr)