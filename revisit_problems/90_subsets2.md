
---

## 🔁 Subsets II — Revision Notes (Iterative Approach with Duplicates)
problem : (https://leetcode.com/problems/subsets-ii)
---

### 🟠 **Brute Force Logic (Iterative)**

* Start with `res = [[]]` (contains the empty subset).
* Loop through each number in `nums`.
* For each number:

  * Create new subsets by adding the number to all **existing subsets**.
  * If it's a **duplicate**, only add to subsets formed in the **previous step** (not the full list).
* Add the new subsets to the result.

---

### ❌ Where I Went Wrong

#### 1. **Forgot to Sort `nums`**

* 🔸 The duplicate check `nums[i] == nums[i - 1]` only works **after sorting**
* ✅ Always sort `nums` first to group duplicates together.

---

#### 2. **Set `start = len(res)` too early**

* 🔸 I updated `start` **before** extending `res`, so next iteration's `start` value was wrong.
* ✅ Update `start = len(res)` **after** extending — to mark where new subsets began.

---

### ✅ Clean Logic Summary

| Step                | What to Do                                                                 |
| ------------------- | -------------------------------------------------------------------------- |
| Sort `nums`         | Required for duplicate check                                               |
| Track `start` index | To know where the last layer of subsets began                              |
| On duplicate        | Only add to new subsets formed in last step (from `start` to end of `res`) |
| On unique           | Add to **all** subsets (`start = 0`)                                       |
| After each `i`      | Update `start = len(res)` (after extending)                                |

---

Optimized verison:(backtracking):

  - same as subset problem.just need include few steps. mandatory to remember to sort the array.
  - for i in range(start,len(nums)):
        if i > start and nums[i-1] == nums[i]:
            continue
  - step to skip duplicates. and remaining is just like a copy of previous subset problem(78).
