from trees.tree_node import TreeNode


def longest_uni_value_path(root: TreeNode):
    """
    1. if I am a leaf, and have children then:
        a. I could be part of the longest path
        b. my children are part of the longest path
        c. my children are not part of the longest path, but I am
        d. neither me nor my children are part of the longest path
    2. if b is true, a global value has that value
    3. if both leaf and children are part, and recursively then add the size
    4. if I am part and the children are not then its just me
    5. note, need to take of the left and right separately, as one of them could be
    :param root:
    :return:
    """
    if not root:
        return 1
    longest_uni_value_path_result = list()
    longest_uni_value_path_result[0] = 1

    def longest_uni_value_path_helper(leaf: TreeNode):
        longest_path = 0 # calculate the longest univalue path depth from here
        longest_v_path = 0 # calculate the inverted v path
        if leaf.right is None and leaf.left is None:
            pass # can't do anything on a leaf node
        if leaf.left is not None:
            longest_left_path = longest_uni_value_path_helper(leaf.left)
            if leaf.left.val == leaf.val:
                longest_path = 1 + longest_left_path
                longest_v_path = longest_path # left of the tree is going to be the same
        if leaf.right is not None:
            longest_right_path = longest_uni_value_path_helper(leaf.right)
            if leaf.right.val == leaf.val:
                longest_path = max(longest_path, 1 + longest_right_path)
                longest_v_path += 1 + longest_right_path #left path + right path

        longest_uni_value_path_result[0] = max(longest_uni_value_path_result[0], longest_v_path)
        return longest_path # this is the depth


    longest_uni_value_path_helper(root)
    return longest_uni_value_path_result[0]