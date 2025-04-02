from stacks_queues_linkedlists.linked_list_basics import Node


def merge_two_sorted_linked_lists(l1: Node , l2: Node):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next


def merge_two_sorted_linked_lists_revision(l1: Node, l2: Node):
    dummy = Node(data=0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

def create_linked_list(arr: list):
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = Node(data=arr[i])
        cur = cur.next
    return head

def print_list(head: Node):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    return '->'.join(result)

if __name__ == '__main__':
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted_linked_lists_revision(list1, list2)
    print(f"Merged list: {print_list(merged)}")



