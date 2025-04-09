from leetcode.blackline.level_order_traversal import TreeNode


def disk_dir_sum(root: TreeNode) -> int:
    """
        given the root or head of a disk or directory, calculate the total space occupied
        by its child directories and files
    :param root:
    :return:
    """
    if not root:
        return 0
    du = root.val
    if root.right:
        du += disk_dir_sum(root=root.right)
    if root.left:
        du += disk_dir_sum(root=root.left)
    return du