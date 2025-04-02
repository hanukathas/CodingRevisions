from xml.etree.ElementPath import prepare_descendant

from stacks_queues_linkedlists.linked_list_basics import Node


def reverse_subset_llist(head: Node, left, right):
    dummy = Node(0, head)
    prev, cur = None, head
    index = 1
    while index != left:
        prev = cur
        cur = cur.next
        index += 1

    tail_left = prev
    tail_middle = cur
    prev.next = None

    while index != right + 1:
        index += 1
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    head_middle = prev
    head_right = cur

    tail_left.next = head_middle
    tail_middle.next = head_right
    return  dummy.next

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

if __name__ == '__main__':
    test_list = create_linked_list([3,6,9,2,4,7,10,11])
    print(f"Original list: {print_list(test_list)}")
    sorted_list = reverse_subset_llist(test_list, 2,6)
    print(f"Sorted list: {print_list(sorted_list)}")
