==================================================================
🧩 Problem: Remove Nth Node From End of List  
🔗 Link    : https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
📚 Topic   : Linked List  
📈 Level   : Medium  
==================================================================

📄 Description:  
Given the head of a linked list, remove the nth node from the end of the list and return its head.

📌 Example:  
Input  : head = [1,2,3,4,5], n = 2  
Output : [1,2,3,5]  

==================================================================
🧠 My Initial Idea:  

- Find the **nth node from end** using two pointers:
  - First pointer (`fast`) moves `n` steps ahead.
  - Second pointer (`slow`) starts from head.
  - Move both together until `fast` reaches the end.
  - Now `slow` is just before the node to delete.

Diagram:
```
head: 1 → 2 → 3 → 4 → 5 → None
           ↑         ↑
         slow       fast (after n steps)
```

------> before solving this have idea on problems :  
- [Linked List Basics] → building, deleting, and traversing  
- [Two Pointer Technique] → for relative distance traversal  

🪜 STEPS :  

step1 : Move `fast` pointer `n` steps ahead.

```python
dummy = ListNode(0)
dummy.next = head
fast = slow = dummy

for _ in range(n):
    fast = fast.next
```

❌ Mistake: If `n` is exactly the length of the list, fast will reach the end, so we need a dummy node.  
✅ Fix   : Introduced a `dummy` node pointing to head to handle edge cases like deleting the first node.

step2 : Move both `fast` and `slow` together until `fast.next` is None.

```python
while fast.next:
    fast = fast.next
    slow = slow.next
```

step3 : Delete the node after `slow`.

```python
slow.next = slow.next.next
```

❌ Mistake: Without dummy node, deleting the head node becomes tricky.  
✅ Fix   : `dummy.next = head` makes it consistent and easy to return new head.

===============================================================================

🚧 Where I Went Wrong:

| Mistake (❌)                                 | Fix (✅)                                   |
| ------------------------------------------- | ------------------------------------------ |
| No dummy node → issues with head removal    | Added dummy node to handle edge cases      |
| Confusion with fast/slow indexing           | Visual dry-run helped understand movement  |

===============================================================================
```python
# 💻 Final Code

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

==================================================================
🧪 Test Case:  
Input : head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]  

📝 Notes:
- Edge case: n == length → delete head
- Always use a dummy node when deleting a node from linked list
- Variants:
  - Delete middle node
  - Remove duplicates from sorted list
==================================================================
