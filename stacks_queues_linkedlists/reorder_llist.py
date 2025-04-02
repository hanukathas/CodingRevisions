from stacks_queues_linkedlists.linked_list_basics import Node


def mid_point(head: Node):
    """
    1. divide the list in to two halves - head n tortoise
    2. reverse the second the list - assign a dummy to break
    3. merge the two sorts - just add the last
    :param head:
    :return:
    """
    if not head or not head.next:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if not fast or not fast.next:
            return slow

    return slow


def reverse_llist(head: Node):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def merge_two_llist(l1: Node, l2: Node):
    dummy = Node(0)
    cur = dummy

    while l1 and l1.next:
        cur.next = l1
        cur = l1
        l1 = l1.next
        cur.next = l2
        cur = l2
        l2 = l2.next

    if l2:
        cur.next = l2
        cur = l2
    return dummy.next


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
    # test_list = create_linked_list([3, 6, 9, 2, 4, 7, 10, 11])
    test_list = create_linked_list([1,2,3,4,5])
    print(f"Original list: {print_list(test_list)}")
    right_list = mid_point(test_list)
    print(f"right list: {print_list(right_list)}")
    reversed_list = reverse_llist(right_list)
    print(f"reversed list: {print_list(reversed_list)}")
    merged_list = merge_two_llist(test_list, reversed_list)
    print(f"Sorted list: {print_list(merged_list)}")


