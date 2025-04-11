from trees.tree_node import TreeNode


def build_tree(arr:list):
    if len(arr) == 0:
        return TreeNode(val="0")

    def helper(A,start, end):
        if start > end:
            return TreeNode(val="null")

        if start == end:
            return TreeNode(val=str(A[0]))

        mid = start + (end - start) // 2
        root_node = TreeNode(val=str(A[mid]))
        root_node.left = helper(A[0:mid], 0, mid)
        root_node.right = helper(A[mid:len(arr)], mid+1, len(arr))
        return root_node


    return helper(arr, 0, len(arr) - 1)
