from stacks_queues_linkedlists.linked_list_basics import Node


def reverse_linked_list(head: Node):
    prev, cur = None, head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

def reverse_linked_list_revision(head: Node):
    prev, cur = None, head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

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
    test_list = create_linked_list([4, 2, 1, 3])
    print(f"Original list: {print_list(test_list)}")
    sorted_list = reverse_linked_list_revision(test_list)
    print(f"Sorted list: {print_list(sorted_list)}")  # Output: 1->2->3->4