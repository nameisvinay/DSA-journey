
```markdown
# 🧠 Problem: Median of Two Sorted Arrays

### Leetcode Link: [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## ✅ Problem Summary

Given two sorted arrays `nums1` and `nums2`, return the **median** of the merged array in `O(log(min(n, m)))` time.

---

## 🚀 Intuition Behind the Binary Search Approach

Instead of merging arrays (which is `O(n+m)`), we can apply **binary search** on the **smaller array**, and partition both arrays at suitable points so that:

```

max(left half) ≤ min(right half)

````

---

## 📌 Goal of Partition

Divide both arrays such that:
- Left half contains the first half of total elements
- Right half contains the rest
- And both halves are **validly ordered**

---

## 🧮 Formula for Partition

Let:
- `m1` = partition index in `nums1` (from binary search)
- `m2` = partition index in `nums2` so that left half has `(n + m + 1) // 2` elements

```python
m2 = (len(nums1) + len(nums2) + 1) // 2 - m1
````

Why +1?

* Ensures correct partitioning for both even/odd total lengths.

---

## 🎯 Conditions to Check

* Let:

```python
l1 = nums1[m1 - 1] if m1 > 0 else float('-inf')
r1 = nums1[m1]     if m1 < len(nums1) else float('inf')

l2 = nums2[m2 - 1] if m2 > 0 else float('-inf')
r2 = nums2[m2]     if m2 < len(nums2) else float('inf')
```

* Check partition validity:

```python
if l1 <= r2 and l2 <= r1:
    # valid partition
```

* Else, move binary search window:

```python
if l1 > r2:
    h = m1 - 1  # move left
else:
    l = m1 + 1  # move right
```

---

## 🖼️ Visual Illustration

### Example:

```python
nums1 = [1, 3]
nums2 = [2, 4, 5, 6]
```

Total elements = 6 → Half = 3

### Let's say:

* `m1 = 1` → partitioning `nums1` as `[1] | [3]`
* `m2 = 2` → partitioning `nums2` as `[2, 4] | [5, 6]`

```
nums1:   [1] | [3]
nums2: [2, 4] | [5, 6]
           ↑     ↑
         l1=1   r1=3
         l2=4   r2=5
```

Check:

```
l1 <= r2 → 1 <= 5 ✅
l2 <= r1 → 4 <= 3 ❌
```

Not valid → so we need to **move m1 right** → `l = m1 + 1`

---

## ⚠️ Edge Case Handling

1. **Empty Array:**

```python
nums1 = [], nums2 = [1, 2, 3]
```

→ `m1 = 0`, so `l1 = -inf`, `r1 = inf` → prevents index error

2. **m1 = 0** or **m1 = len(nums1)**:
   We set:

```python
l1 = -inf if m1 == 0
r1 = inf  if m1 == len(nums1)
```

3. **Always binary search on the smaller array**

```python
if len(nums1) > len(nums2):
    return self.findMedianSortedArrays(nums2, nums1)
```

---

## ✅ Code: Python (with edge safety)

```python
def findMedianSortedArrays(self, nums1, nums2):
    if len(nums1) > len(nums2):
        return self.findMedianSortedArrays(nums2, nums1)

    l, h = 0, len(nums1)

    while l <= h:
        m1 = (l + h) // 2
        m2 = (len(nums1) + len(nums2) + 1) // 2 - m1 # +1 to handle even and odd 

        #handling of out of bounds if m1 goes beyond 0 then take min as float('-inf')
        l1 = nums1[m1 - 1] if m1 > 0 else float('-inf')
        r1 = nums1[m1] if m1 < len(nums1) else float('inf')

        l2 = nums2[m2 - 1] if m2 > 0 else float('-inf')
        r2 = nums2[m2] if m2 < len(nums2) else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (len(nums1) + len(nums2)) % 2 == 0: #length is even so take below
                return (max(l1, l2) + min(r1, r2)) / 2
            else:  #length is odd so pick max(l1,l2)
                return max(l1, l2)
        elif l1 > r2:
            h = m1 - 1
        else:
            l = m1 + 1
```

---

## 🧪 Test Cases

```python
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5

Input: nums1 = [], nums2 = [1]
Output: 1.0

Input: nums1 = [2], nums2 = []
Output: 2.0
```

---

## 🧠 Time & Space Complexity

| Type  | Value               |
| ----- | ------------------- |
| Time  | `O(log(min(n, m)))` |
| Space | `O(1)`              |

---

## ✅ Summary

* Use binary search on the **shorter array**
* Carefully partition both arrays
* Handle edge cases using `float('-inf')` / `float('inf')`
* Make sure to avoid index errors at boundary conditions

```

---
