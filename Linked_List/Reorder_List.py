"""
🧩 Problem: Reorder List  
🔗 Leetcode: https://leetcode.com/problems/reorder-list/  
📘 Category: Linked List  
📈 Difficulty: Medium

---

📝 Problem Statement:
You are given the head of a singly linked list.  
Reorder the list in-place as:  
`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`

### Example:
Input:  1 -> 2 -> 3 -> 4 -> 5  
Output: 1 -> 5 -> 2 -> 4 -> 3

Constraints:
- Do not modify the values in the list’s nodes, only the pointers.

---

🚀 My Thought Process:
1. This looks like combining first and last, second and second last, etc.
2. I thought of **splitting the list into two halves**.
3. Then **reversing the second half**.
4. Finally, **merging** both halves alternatively.

---

🧗 Where I Got Stuck:
- My code didn’t work when I used `mid` instead of `mid + 1`.
- In some cases, I didn’t properly disconnect the two halves — it formed a cycle.
- Forgot to `prev.next = None` after finding the middle to separate halves.

---

✅ Modifications I Did:
- Used slow and fast pointer to find the middle.
- Broke the list into two parts with `prev.next = None`.
- Reversed the second half.
- Carefully merged both lists node by node.

---

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None  # Break the list into two halves

    # Step 2: Reverse second half
    prev_rev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev_rev
        prev_rev = curr
        curr = next_temp

    # Step 3: Merge both halves
    first, second = head, prev_rev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        if tmp1 is None:
            break
        second.next = tmp1
        first, second = tmp1, tmp2

"""
🧪 Test Case:
Input:  [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

🧠 Notes:
- Useful for questions involving LL manipulation in-place.
- Mastering this helps in problems like:
  - Palindrome Linked List
  - Rearranging Odd-Even LL
"""
