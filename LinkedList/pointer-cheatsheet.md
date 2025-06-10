# 🧠 Linked List Pointer Cheatsheet (Fast Intuition Guide)

---

## 🔁 1. Find Middle of Linked List

**Pattern**: Slow & Fast pointers (Tortoise-Hare)

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow  # middle node
```

**Use when**: You want to split the list, or check symmetry/palindrome.

---

## 🔀 2. Detect Cycle

**Pattern**: Same as above, but check if `slow == fast`

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

**Use when**: You want to know if the list loops back.

---

## ⏪ 3. Reverse a Linked List

**Pattern**: `prev`, `curr`, `next`

```python
prev = None
curr = head
while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
return prev  # new head
```

**Use when**: You need to reverse entire list or a part of it.

---

## 🎯 4. Remove N-th Node from End

**Pattern**: Two pointers, gap of `n` steps

```python
dummy = Node(0)
dummy.next = head
fast = slow = dummy

# Move fast n+1 steps ahead
for _ in range(n + 1):
    fast = fast.next

while fast:
    slow = slow.next
    fast = fast.next

slow.next = slow.next.next
return dummy.next
```

**Use when**: You want to remove or access a node from the end.

---

## ➕ 5. Merge Two Sorted Lists

**Pattern**: Compare and build with dummy node

```python
dummy = Node(0)
tail = dummy

while l1 and l2:
    if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next

tail.next = l1 or l2
return dummy.next
```

**Use when**: Merging sorted lists like in MergeSort or LeetCode #21.

---

## 🪓 6. Split List into Halves

Use `slow` and `fast`, then `slow.next = None` to break the list in two.

---

## 🧪 7. Check if Palindrome

1. Find middle using slow-fast
2. Reverse second half
3. Compare both halves node-by-node

---

## 🪠 Common Tips

| Tip                         | Meaning                                |
| --------------------------- | -------------------------------------- |
| `while fast and fast.next:` | Prevent null pointer issues            |
| Use `dummy` nodes           | Avoid special cases like head deletion |
| Track `next` when reversing | Prevents losing rest of list           |
| Use temp variables          | Helps debug pointer movement           |

---

## 📌 Quick Summary

```text
🧠 Pointer Tricks:
- slow/fast = find mid / detect cycle
- fast ahead = nth from end
- prev-curr-next = reverse
- dummy = safe editing
```

---
