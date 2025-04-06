from os.path import curdir
from pdb import line_prefix

from stacks_queues_linkedlists.linked_list_basics import Node


def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(data=val)
        current = current.next
    return head


# Helper function to print linked list
def print_list(head: Node):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    return '->'.join(result)


def reverse_llist(head: Node):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def reverse_nodes_k_group(head: Node, k: int):
    local_head = head
    dummy = Node(data=0)
    tail = dummy

    while local_head and local_head.next:
        index = 1
        pointer = Node(data=local_head.data)
        local_cur = pointer
        while index < k and local_head and local_head.next:
            print(local_head.data, index)
            local_head = local_head.next
            local_cur.next = Node(data=local_head.data)
            local_cur = local_cur.next
            index += 1

        tail.next = reverse_llist(pointer)
        while tail and tail.next:
            tail = tail.next
        local_head = local_head.next

    return dummy.next

def reverse_nodes_k_size(head: Node, k: int):
    local_head = head
    dummy = Node(data=0)
    tail = dummy

    while local_head and local_head.next:
        index = 1
        pointer = Node(data=local_head.data)
        local_cur = pointer
        while index < k and local_head and local_head.next:
            local_head = local_head.next
            local_cur.next = Node(data=local_head.data)
            local_cur = local_cur.next
            index += 1
        tail.next = reverse_llist(pointer)
        while tail and tail.next:
            tail = tail.next
        local_head = local_head.next
    return dummy.next




if __name__ == '__main__':
    # test_list = create_linked_list([3, 6, 9, 2, 4, 7, 10, 11])
    test_list = create_linked_list([1, 2, 3, 4, 5, 6])
    print(f"Original list: {print_list(test_list)}")
    final_list = reverse_nodes_k_size(test_list, 4)
    print(f"Reversed list: {print_list(final_list)}")
    final_list = reverse_nodes_k_group(test_list, 4)
    print(f"Reversed list: {print_list(final_list)}")
