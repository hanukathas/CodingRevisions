from ctypes.wintypes import tagMSG

from stacks_queues_linkedlists.linked_list_basics import Node


def insertion_sort_list(head: Node):
    dummy = Node(0, head)
    prev, cur = head, head.next

    while cur:
        while cur.data >= prev.data:
            prev, cur = cur, cur.next
            continue

        tmp = dummy
        while cur.data > tmp.next.data:
            tmp = tmp.next

        prev.next = cur.next
        cur.next = tmp.next
        tmp = cur.next
        cur = prev.next
    return dummy.next

def insertion_sort_list_revision(head: Node):
    dummy = Node(0, head)
    prev, cur = head, head.next
    while cur:
        while cur.data >= prev.data:
            prev = cur
            cur = cur.next
            continue
        tmp = dummy
        while cur.data >= tmp.next.data:
            tmp = tmp.next

        prev.next = cur.next
        cur.next = tmp.next
        tmp.next = cur
        cur = prev.next
    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(data= arr[0])
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
    sorted_list = insertion_sort_list_revision(test_list)
    print(f"Sorted list: {print_list(sorted_list)}")