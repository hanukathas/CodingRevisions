from typing import SupportsInt

from trees.tree_node import TreeNode


def print_all_paths(root: TreeNode):
    if not root:
        return []

    result = []
    def helper(node: TreeNode, slate: list):
        slate.append(node.val)
        if node.right is None and node.left is None:
            result.append(slate[:])
        if node.left is not None:
            helper(node.left, slate)
        if node.right is not None:
            helper(node.right, slate)
        slate.pop()
    helper(root, [])
    return result

def print_all_paths_r(root: TreeNode):
    """
    print all path from a given node
    note: when you append to a slate, pop too at the end
    :param root:
    :return:
    """
    result = []
    def printer(leaf: TreeNode, slate: []):
        slate.append(leaf.val)
        if leaf.right is None and leaf.left is None:
            result.append(slate[:])
        if leaf.left is not None:
            print(leaf.left, slate)
        if leaf.right is not None:
            print(leaf.right, slate)
        slate.pop()
    return result

def longest_path(root: TreeNode):
    if not root:
        return []
    result = []
    def helper(leaf: TreeNode, length_thus_far: int):
        length_thus_far += 1
        if leaf.right is None and leaf.left is None:
            return result.append(length_thus_far - 1)
        if leaf.left is not None:
            helper(leaf.left, length_thus_far)
        if leaf.right is not None:
            helper(leaf.right, length_thus_far)
        length_thus_far -= 1

    helper(root, 0)
    return max(result)

def longest_consecutive_sequence(root:TreeNode):
    if not root:
        return 0
    result = [0]
    def helper(leaf: TreeNode, prev_val: int, count_so_far: int):
        if prev_val + 1 == leaf.val:
            count_so_far += 1
            result[0] = max(count_so_far, result[0])
        else:
            count_so_far = 1
        if leaf.right is None or leaf.left is None:
            pass
        if leaf.left is not None:
            helper(leaf.left, int(leaf.val), count_so_far)
        if leaf.right is not None:
            helper(leaf.right, leaf.val, count_so_far)

    helper(root, int(root.val), 0)
    return result[0]