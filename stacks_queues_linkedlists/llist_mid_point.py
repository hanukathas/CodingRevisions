class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    # Handle empty list or single node
    if not head or not head.next:
        return head

    # Initialize tortoise and hare pointers
    slow = head
    fast = head

    # Move tortoise one step and hare two steps
    while fast and fast.next:
        slow = slow.next  # Move one step
        fast = fast.next.next  # Move two steps

        # When fast reaches end, slow is at middle
        if not fast or not fast.next:
            return slow

    return slow

def mid_row(head):
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


# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == '__main__':
# Test the function
    test_list = create_linked_list([1, 2, 3, 4, 5])
    middle = mid_row(test_list)
    print(f"Middle node value: {middle.val}")  # Output: 3