

```markdown
==================================================================
🧩 Problem: Median of Two Sorted Arrays  
🔗 Link    : https://leetcode.com/problems/median-of-two-sorted-arrays/  
📚 Topic   : Binary Search, Divide and Conquer  
📈 Level   : Hard  
==================================================================

📄 Description:  
Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the **median** of the two sorted arrays.  
The overall run time complexity should be **O(log(min(m, n)))**.

---

## ✅ My Understanding:

At first, I thought of merging both arrays and finding the median. But that takes **O(n + m)** time — too slow for large inputs.  
So I looked for an optimized approach and found the **binary search on partition** trick.

---

## 🧠 Key Idea:

Use **binary search** on the **shorter array**, and find a partition such that:

```

max(left part) <= min(right part)

````

Let:
- `m1` = partition in `nums1`
- `m2` = derived partition in `nums2` such that left half has `(n + m + 1) // 2` elements
- Use `float('-inf')` and `float('inf')` to handle out-of-bound edge cases

We maintain:
```python
l1 = nums1[m1-1] if m1 > 0 else -inf
r1 = nums1[m1]   if m1 < len(nums1) else inf

l2 = nums2[m2-1] if m2 > 0 else -inf
r2 = nums2[m2]   if m2 < len(nums2) else inf
````

---

## 🔄 Binary Search Steps (My Thought Process):

1. Always binary search on the **smaller array**
2. Calculate `m1` and `m2` to partition both arrays
3. Check if:

   * `l1 <= r2` and `l2 <= r1` → valid partition
   * If total length is even → return average of `max(l1, l2)` and `min(r1, r2)`
   * If odd → return `max(l1, l2)`
4. If partition is not valid:

   * If `l1 > r2`, move left → `h = m1 - 1`
   * Else, move right → `l = m1 + 1`

---

## ⚠️ Bug I Faced Initially:

I was mistakenly updating `h = m2 - 1` instead of `h = m1 - 1`, which is incorrect since binary search is on `nums1`.
Also missed handling edge cases like when `nums1 = []` — caused index errors.
✅ Fixed it by guarding edges with `-inf` and `inf`.

---

## ✅ Final Code (Accepted):

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        return self.findMedianSortedArrays(nums2, nums1)

    l, h = 0, len(nums1)

    while l <= h:
        m1 = (l + h) // 2
        m2 = (len(nums1) + len(nums2) + 1) // 2 - m1

        l1 = nums1[m1 - 1] if m1 > 0 else float('-inf')
        r1 = nums1[m1]     if m1 < len(nums1) else float('inf')

        l2 = nums2[m2 - 1] if m2 > 0 else float('-inf')
        r2 = nums2[m2]     if m2 < len(nums2) else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (len(nums1) + len(nums2)) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
        elif l1 > r2:
            h = m1 - 1
        else:
            l = m1 + 1
```

---

## 🔍 Dry Run (Example):

```python
nums1 = [1, 3]
nums2 = [2]

Total length = 3 → half = 2
m1 = 1, m2 = 1

nums1: [1] | [3]
nums2: [2] | []

l1 = 1, r1 = 3
l2 = 2, r2 = inf

Check: l1 <= r2 and l2 <= r1 → 1 <= inf and 2 <= 3 ✅
Total is odd → return max(l1, l2) = max(1, 2) = 2
```

---

## 💡 What I Learned:

* Do binary search on the smaller array only
* Use virtual `-inf` and `inf` for out-of-bounds on edges
* Use total size formula `(n + m + 1) // 2` to divide left & right
* Dry run edge cases like:

  * `nums1 = []`, `nums2 = [1]`
  * Even vs odd total lengths

---
