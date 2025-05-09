"""
Asymptotic complexity in terms of the number of nodes in the BST `n` and the size of the input list `m`:
* Time: O(n * m).
* Auxiliary space: O(n).
* Total space: O(n + m).
"""
from trees.tree_node import TreeNode
from trie.multi_copy_trie import TrieNode


def delete_from_bst_helper(root, key):
    if root is None:
        return root

    # Searching for a node with the given value.
    if key < root.value:
        root.left = delete_from_bst_helper(root.left, key)
    elif key > root.value:
        root.right = delete_from_bst_helper(root.right, key)
    else:
        # If the node to be deleted is a leaf node, then we will be replacing it with a NULL node.
        if root.left is None and root.right is None:
            del root
            return None

        # If the node to be deleted has only one child, then we will be replacing it with its non-NULL child.
        if root.left is None:
            temp = root.right
            del root
            return temp
        if root.right is None:
            temp = root.left
            del root
            return temp

        # If the node to be deleted has two child nodes, then we will be replacing its value with that of its
        # inorder successor and recursively delete the inorder successor.
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.value = temp.value
        root.right = delete_from_bst_helper(root.right, temp.value)

    return root

def delete_from_bst(root, values_to_be_deleted):
    if root is None or len(values_to_be_deleted) == 0:
        return root

    for value in values_to_be_deleted:
        root = delete_from_bst_helper(root, value)
        root = delete_from_bst_helper_r(root, value)

    return root

def delete_from_bst_helper_r(leaf: TreeNode, value: int):
    if value < leaf.val:
        delete_from_bst_helper_r(leaf.left, value)

    if value > leaf.val:
        delete_from_bst_helper_r(leaf.right, value)

    if value == leaf.val:
        if leaf.left is None and leaf.right is None:
            del leaf
        elif leaf.left is None and leaf.right is not None:
            pass





