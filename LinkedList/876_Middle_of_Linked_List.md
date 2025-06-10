# 🧠 LeetCode 876 - Middle of the Linked List

**Problem Link**: [LeetCode 876](https://leetcode.com/problems/middle-of-the-linked-list/)

---

## 🧩 Goal:
Given the head of a singly linked list, return the middle node.  
If there are two middle nodes, return the second one.

---

## 🔍 Initial Approach (Count & Traverse)

### ✅ Thought:
1. Count the total number of nodes.
2. If length is even: middle = length // 2  
   If odd: middle = (length // 2) + 1
3. Traverse again to reach middle node.

### ❌ Mistake:
I lost the head in first loop and reused it again.

```python
count = 0
while head:
    count += 1
    head = head.next   # ⛔ head became None here

# reused head in second loop → bug
while head:  # head is None now
    ...

