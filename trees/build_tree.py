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
