from trees.tree_node import TreeNode

def valid_bst_recursive(root: TreeNode):
    if root is None:
        return True

    min_val = float('-inf')
    max_val = float('inf')

    def valid_bst_recursive_helper(leaf: TreeNode, min_val: float, max_val:float):
        if leaf is None:
            return True
        if leaf.val < min_val or leaf.val > max_val:
            return False
        return valid_bst_recursive_helper(leaf.left, min_val, leaf.val) and valid_bst_recursive_helper(leaf.right, leaf.val, max_val)
    return valid_bst_recursive_helper(root, min_val, max_val)

def valid_bst_bit_wise(root: TreeNode):
    if root is None:
        return True
    prev = [float('-inf')]

    def helper(leaf: TreeNode, prev_node_val):
        if leaf is None:
            return True

        is_left_bst_tree = helper(leaf.left, prev_node_val)

        if leaf.val < prev_node_val:
            return False
        prev_node_val = leaf.val

        is_right_bst_tree = helper(leaf.right, prev_node_val)

        return is_left_bst_tree and is_right_bst_tree



def valid_bst_dont_use(root: TreeNode):
    if not root:
        return  True
    valid_bst_result = list()
    def valid_bst_helper(leaf: TreeNode):
        """
            here we evaluate strictly if the child tree is BST or not.
            going by BST definition:
            1. if it is a leaf then nothing matters
            2. if it is not a leaf, it should both left and right leaves
            3. if it has left and right leaves, left.val < right.val
            4. recursively, left and right children are also BSTs
            5. so in recursion terms, the largest of left is less than root, smallest right val is greater than root

        :param leaf:
        :return:
        """
        is_valid_bst = True
        smallest_val = largest_val = int(leaf.val) # I am the root, check against my val

        if leaf.right is None and leaf.left is None:
            pass # a leaf node, nothing matters

        if leaf.left is not None:
            s, l, bst = valid_bst_helper(leaf.left)
            smallest_val = min(smallest_val, s)
            largest_val = max(largest_val, l)
            if not bst or l < int(leaf.val):
                is_valid_bst = is_valid_bst and bst
        if leaf.right is not None:
            s, l, bst = valid_bst_helper(leaf.right)
            smallest_val = min(smallest_val, s)
            largest_val = max(largest_val, l)
            if not bst or leaf.val > s:
                is_valid_bst = is_valid_bst and bst

        valid_bst_result[0] = is_valid_bst

        return smallest_val, largest_val, is_valid_bst

    valid_bst_helper(root)
    return valid_bst_result
