## 🧠 Problem: Reverse Linked List (LeetCode 206)

### ❌ First Attempt
```python
dummy = None
while head.next:
    head.next = dummy
    dummy = head
    head = head.next

❌ head.next = dummy changes pointer before saving the next node
❌ Using while head.next skips the last node
