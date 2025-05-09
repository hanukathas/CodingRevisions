from trees.binary_tree_tile import binary_tree_tile_r
from trees.tree_node import TreeNode


def build_tree(arr:list):
    if len(arr) == 0:
        return TreeNode(val="0")

    def helper(A,start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(val=A[0])
        mid = (end - start) // 2
        root = TreeNode(val=A[mid])
        root.left = helper(A, 0, mid-1)
        root.right = helper(A, mid+1, end)

        return root
    return helper(arr, 0, len(arr) - 1)

def build_tree_r(arr:list):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2

    root = TreeNode(val=arr[mid])
    root.left = build_tree_r(arr[start:mid])
    root.right = build_tree_r(arr[mid+1:])

    return  root

def build_tree_r2(arr:list):
    if len(arr) == 0:
        return None
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    root = TreeNode(val= arr[mid])
    root.right = build_tree_r2(arr[mid+1:])
    root.left = build_tree_r(arr[:mid])
    return root

