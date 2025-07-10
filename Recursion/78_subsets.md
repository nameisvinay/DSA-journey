
````markdown
==================================================================
🧩 Problem: Subsets (Power Set Generation)
🔗 Link    : https://leetcode.com/problems/subsets/
📚 Topic   : Backtracking, Recursion, Bitmasking
📈 Level   : Medium
==================================================================

📄 Description:
Given an integer array `nums` of unique elements, return **all possible subsets (the power set)**.  
The solution **must not contain duplicate subsets**, and you may return the answer in **any order**.

---

## ✅ Brute-force Iterative Approach

### 🔧 Code:
```python
def subsets(nums):
    result = [[]]
    for num in nums:
        subset = []
        for char in result:
            subset.append(char + [num])
        result.extend(subset)
    return result
````

### 🔍 How It Works:

Let's say `nums = [1, 2, 3]`

* Start with: `result = [[]]`

* For `1`:
  → Add `1` to all existing subsets: `[] + [1]` → `[1]`
  → Now `result = [[], [1]]`

* For `2`:
  → Add `2` to all existing:

  * `[] + [2]` → `[2]`, `[1] + [2]` → `[1, 2]`
    → `result = [[], [1], [2], [1, 2]]`

* For `3`:
  → Add `3` to all:

  * `[] + [3]`, `[1] + [3]`, `[2] + [3]`, `[1, 2] + [3]`
    → Final Result:

```
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

### 🧠 Key Insight:

* This method doubles the subsets at each step.
* No recursion or backtracking.
* It’s clean and works in **O(2^n)** time.

---

## 🔁 Recursive Backtracking Approach

```python
def subsets(nums):
    res = []
    subset = []

    def backtrack(start):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
    
    backtrack(0)
    return res
```

---

## 🔍 Dry Run With Example

Let `nums = [1, 2, 3]`

```text
Call: start = 0, subset = []

→ Append [] to result

  → Add 1 → subset = [1]
    → Add 2 → subset = [1, 2]
      → Add 3 → subset = [1, 2, 3] → hit base → save it
      → Pop 3 → subset = [1, 2]
    → Pop 2 → subset = [1]
    → Add 3 → subset = [1, 3] → save
    → Pop 3 → subset = [1]
  → Pop 1 → subset = []

→ Add 2 → subset = [2]
  → Add 3 → subset = [2, 3]
  → Pop 3 → [2]
→ Pop 2 → []

→ Add 3 → [3] → save
→ Pop 3 → []

→ Done
```

---

## ❓ Confusing Part I Faced:

| Doubt                                                       | Realization                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------- |
| After pop(), don’t we revisit same element?                 | No — control returns to previous loop where we move to next i |
| Why do we append before recursive call?                     | That simulates “including” the element                        |
| Why subset.pop()?                                           | To **undo** the choice for the next recursion path            |
| When do we save result?                                     | At every recursive call before the loop                       |
| Do we need to check base case like `if start == len(nums)`? | No. Appending at each call naturally covers all paths         |

---

## 📺 YouTube References (Helped Me Understand Clearly):

1. 🔗 [https://www.youtube.com/watch?v=otFWTk-9b7g](https://www.youtube.com/watch?v=otFWTk-9b7g)
   ➤ Helped understand recursive flow and backtracking visually.

2. 🔗 [https://www.youtube.com/watch?v=3tpjp5h3M6Y\&t=648s](https://www.youtube.com/watch?v=3tpjp5h3M6Y&t=648s)
   ➤ Showed clear dry run using pen & paper + call stack explanation.

---

## 💡 What I Learned:

* **Brute-force iteration** builds subsets level by level.
* **Backtracking** gives more control and flexibility — especially for advanced problems like combinations, permutations, or constraints.
* Always make a **copy of the subset** before adding to result.
* **Dry runs reveal everything** — even more than code sometimes.
* Subset generation = **Include → Recurse → Pop (Exclude)** pattern

---

## 📌 Summary

| Approach                      | Time        | Space  | Notes                       |
| ----------------------------- | ----------- | ------ | --------------------------- |
| Brute Iterative               | O(2^n)      | O(2^n) | Doubles result at each step |
| Recursive Backtracking        | O(2^n)      | O(n)   | Go deep, explore, pop back  |
| Bitmasking (not covered here) | O(2^n \* n) | O(1)   | Uses binary representation  |

---
