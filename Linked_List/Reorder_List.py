"""
==================================================================
🧩 Problem: Reorder List
🔗 Link    : https://leetcode.com/problems/reorder-list/
📚 Topic   : Linked List
📈 Level   : Medium
==================================================================

📄 Description:
Reorder the given singly linked list in-place such that:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must not modify the values in the nodes, only node connections.

📌 Example:
Input  : [1, 2, 3, 4, 5]
Output : [1, 5, 2, 4, 3]

==================================================================
🧠 Thought Process:

1. This is a merge of first & last, second & second-last, etc.
2. So, I planned 3 steps:
   - Find the middle of the list.
   - Reverse the second half.
   - Merge both halves alternately.

==================================================================
🚧 Where I Got Stuck:

- ❌ Used `mid` directly instead of `mid + 1`, caused merge issues.
- ❌ Forgot to break the first half → caused infinite loop.
- ❌ Incomplete merge logic → missed edge cases with odd/even length.

==================================================================
✅ Fixes Applied:

- Used `slow` and `fast` pointer to find mid node.
- Did `prev.next = None` to split first half cleanly.
- Reversed second half safely.
- Wrote clear merge logic with temporary pointers.

==================================================================
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find middle using slow-fast
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None  # break list into two parts

    # Step 2: Reverse second half
    prev_rev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev_rev
        prev_rev = curr
        curr = nxt

    # Step 3: Merge two halves
    first, second = head, prev_rev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        if not tmp1:
            break
        second.next = tmp1
        first, second = tmp1, tmp2

"""
==================================================================
🧪 Test Case:
Input : [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

📝 Notes:
- Pointer manipulation heavy — draw on paper helps.
- Variants:
  - Palindrome Linked List
  - Rearranging List in Zig-Zag
==================================================================
"""
