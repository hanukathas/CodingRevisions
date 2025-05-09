from trees.tree_node import TreeNode

def min_element(head: TreeNode):
    if not head:
        return None

    curr = head
    while curr.left:
        if not curr.left:
            return curr.val
        else:
            curr = curr.left

def max_element(head: TreeNode):
    if not head:
        return None

    curr = head
    while curr.right:
        if not curr.right:
            return curr.val
        else:
            curr = curr.right

def min_element_r(head: TreeNode):
    if not head:
        return head
    curr = head
    while curr:
        if curr.left is not None:
            return curr.val
        curr = curr.left

def max_element_r(head: TreeNode):
    if not head:
        return head

    curr = head
    while curr:
        if curr.right is None:
            return curr.val
        curr = curr.right
