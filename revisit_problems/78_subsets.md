78 subset : (https://leetcode.com/problems/subsets/description/)

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

---

## 🔁 Subsets Problem — Revision Notes (Brute Force + Backtracking)

---

### 🟠 **Brute Force Approach (Iterative)**

* Start with an empty list `result = []`
* For each number in `nums`:

  * Create a temporary list `subset = []`
  * Loop over all existing subsets in `result`

    * For each, make a new subset by adding current `num` → `res + [num]`
    * Add it to `subset`
  * After inner loop, **extend** `result` with `subset`

#### ❌ Mistakes I Made:

* Used `.append()` instead of `.extend()`
  → `.append()` adds a list as a single item, `.extend()` merges contents
* Tried `res + [num]` on an empty `result`
  → No initial subset to build from — nothing happens
* Fix: Initialize with `result = [[]]` so the loop has a base to build on

---

### 🟢 **Optimized Approach — Backtracking**

* Begin with `res = []`, `result = []`
* Start by **adding an empty subset** (`res.copy()`) to `result`
* Recursively:

  * Add current number to `res`
  * Recurse with `i + 1` (go to next index)
  * After recursion, `pop()` to backtrack and explore other paths
* This continues until all combinations are explored

---

### ⚠️ **Where I Got Stuck (Mistakes in Backtracking)**

| Mistake                  | ❌ What I Did                   | ✅ Correct Way                                         |
| ------------------------ | ------------------------------ | ----------------------------------------------------- |
| **Reference Issue**      | Used `result.append(res)`      | Use `res.copy()` to store snapshot                    |
| **Wrong Index Movement** | Used `backtrack(start + 1)`    | Should be `backtrack(i + 1)` inside loop              |
| **Invalid Condition**    | Checked `if i == len(nums)`    | `i` is undefined — use `start == len(nums)` if needed |
| **Duplicate Appends**    | Appended result multiple times | Only append once per state (top of `backtrack`)       |

---
