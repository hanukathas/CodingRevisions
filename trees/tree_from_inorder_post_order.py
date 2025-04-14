from trees.tree_node import TreeNode


def tree_from_inorder_post_order(In: list, Post: list):
    start_in = In[0]
    end_in = In[len(In) - 1]
    start_post = Post[0]
    end_post = Post[len(Post) - 1]

    if len(In) == len(Post) == 0:
        return TreeNode(val=-1)

    hmap = dict(enumerate(In))


    def tree_from_inorder_post_order_helper(In, start_in, end_in, Post,  start_post, end_post):
        if start_post > end_post:
            return TreeNode(val=-1)

        if start_post == end_post:
            return TreeNode(val=Post[start_post])

        mid = start_in + (end_in - start_in) // 2
        root_index = hmap[mid]
        nums_left = root_index - start_in
        root = TreeNode(val=In[mid])
        root.left = tree_from_inorder_post_order_helper(In, start_in, root_index-1, Post, start_post, start_post+nums_left-1)
        root.right = tree_from_inorder_post_order_helper(In, root_index+1, end_in, Post, start_post+nums_left, end_post-1)
        return root


    return tree_from_inorder_post_order_helper(In, 0, len(In) - 1, Post, 0, len(Post) - 1)






