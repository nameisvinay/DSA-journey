# Leetcode 92 - Reverse Linked List II
# Time: O(n), Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    reversed_tail = curr
    reversed_head = None

    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = reversed_head
        reversed_head = curr
        curr = next_node

    prev.next = reversed_head
    reversed_tail.next = curr

    return dummy.next

