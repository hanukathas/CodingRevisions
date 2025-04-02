from stacks_queues_linkedlists.linked_list_basics import Node


def partition_llist(head: Node, key: int):
    left_dummy = Node(data=0)
    right_dummy = Node(data=0)

    left = left_dummy
    right = right_dummy

    cur = head
    while cur:
        if cur.data < key:
            left.next = cur
            left = left.next
        else:
            right.next = cur
            right = right.next
        cur = cur.next

    right.next = None
    left.next = right_dummy.next

    return left_dummy.next


def create_linked_list(arr):
    if not arr:
        return None
    head = Node(data=arr[0])
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
    test_list = create_linked_list([1, 4, 3, 2, 5, 2])
    print(f"Original list: {print_list(test_list)}")
    partitioned = partition_llist(test_list, 3)
    print(f"Partitioned list: {print_list(partitioned)}")
