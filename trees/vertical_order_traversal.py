from collections import defaultdict
from email.policy import default

from trees.tree_node import TreeNode


def vertical_order_traversal(root: TreeNode): #code where order of leaf elements are not important
    """
    keep an index variable
    as we traverse for left reduce index by 1 and increase by 1 for right
    we can do pre-order traversale
    :param root:
    :return:
    """
    if not root:
        return root
    index = 0
    result = defaultdict(list)
    result = {0: [root.val]}
    def helper(leaf, index):


        if leaf.left is not None:
            left_index = index - 1
            result[left_index].append(leaf.left.val)
            helper(leaf.left, left_index)
        if leaf.right is not None:
            right_index = index + 1
            result[right_index].append(leaf.right.val)
            helper(leaf.right, right_index)


    helper(root, index)
    result = dict(sorted(result.items()))
    return result.values()

def vertical_order_position_traversal(root: TreeNode):# position of element at row level is important
    result = {}
    if not root:
        return []

    def helper(leaf: TreeNode, x:int, y:int):
        if x not in result:
            result[x] = {}
            if y not in result[x]:
                result[x][y] = [leaf.val]
            else:
                result[x][y].add(leaf.val)

        if leaf.left:
            helper(leaf.left, x-1, y+1)
        if leaf.right:
            helper(leaf.right, x+1, y+1)

    helper(root, 0, 0)

    return result

def vertical_order_position_traversal_r(root: TreeNode):
    if not root:
        return []
    result = []
    def traversal(leaf, x, y):
        if x not in result:
            result[0] = {}
            if y not in result[x]:
                result[x][y] = [leaf.val]
            else:
                result[x][y].append(leaf.val)
        if leaf.left is not None:
            traversal(leaf.left, x - 1, y + 1)
        if leaf.right is not None:
            traversal(leaf.left, x + 1, y + 1)
    traversal(root, 0, 0)
    return result

