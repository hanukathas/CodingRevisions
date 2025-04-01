from wsgiref.validate import header_re

from stacks_queues_linkedlists.linked_list_basics import Node


def cycle_detection(node: Node, head: Node) -> bool:
    """
        common sense: color every node visited. when we visit a colored node,
        then we have entered cycle
    :return:
    """
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return  True
    return False
        