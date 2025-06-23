
---

````markdown
==================================================================
🧩 Problem: Sliding Window Maximum
🔗 Link    : https://leetcode.com/problems/sliding-window-maximum/
📚 Topic   : Sliding Window, Deque
📈 Level   : Hard
==================================================================

📄 Description:
Given an integer array `nums` and a sliding window of size `k`, return the maximum value in each window as it slides from left to right.

---

## ✅ My Understanding:

This problem is about keeping track of the **maximum value** in every window of size `k` as we slide from the start to the end of the array.  
At first, I thought of using a brute-force approach (checking max in every window), but that's **too slow** – O(n*k).  
Then I remembered the **Monotonic Queue (Deque)** technique, which gives us O(n) time.

---

## 🧠 Key Idea:

We use a **deque** to keep **indexes** (not values) of useful elements, such that:
- Elements in the deque are in **decreasing order of their values**.
- The **front of the deque** always has the **maximum** for the current window.

---

## 🔄 Sliding Window Steps (My Thought Process):

For each index `i` from 0 to n-1:
1. **Remove from back** all indices where `nums[queue[-1]] < nums[i]`  
   → Because they're smaller and can't be max anymore.
2. **Remove from front** if it's outside the window (`i - k`)  
   → It's not part of the window anymore.
3. **Add current index** `i` to the deque  
   → Could be max for the next windows.
4. **If window size is hit** (`i >= k-1`), add `nums[queue[0]]` to result  
   → That's the current window’s max.

---

## ⚠️ Bug I Faced Initially:

I was checking window size **before** removing out-of-window elements. That caused wrong maximums in some windows.  
I **fixed it by maintaining the order**:  
➤ First clean outdated indices → Then check window size.

---

## ✅ Final Code (Accepted):

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i in range(len(nums)):
            # Step 1: Remove elements smaller than current from the back
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # Step 2: Remove the front if it's out of the window
            if queue and queue[0] == i - k:
                queue.popleft()

            # Step 3: Add current index
            queue.append(i)

            # Step 4: Add to result when window is fully formed
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
````

---

## 🔍 Dry Run (Example):

```
nums  = [1,3,-1,-3,5,3,6,7], k = 3

Window slides like:
[1 3 -1] → max = 3  
[3 -1 -3] → max = 3  
[-1 -3 5] → max = 5  
[-3 5 3] → max = 5  
[5 3 6] → max = 6  
[3 6 7] → max = 7  

Result: [3, 3, 5, 5, 6, 7]
```

---

## 💡 What I Learned:

* Keep deque indices in decreasing value order → ensures max is always in front.
* Always clean out-of-window elements before checking window size.
* Deque helps achieve **O(n)** time for max sliding window.

---

## 📌 Tags:

`Sliding Window` `Deque` `Monotonic Queue` `Two Pointer Variant` `Hard` `Optimized`

```

---

```
