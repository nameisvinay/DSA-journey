###

💡 Next greater:
```
   when we are looking for future elements (next greater), it's better to traverse from right to left(reversed).
```

💡 subsets-II:
```
   len(res) actually gives us the index where we should start forming new subsets in the next step — especially when handling duplicates.
```

💡 Binary search loop condition:
```
    | Use Case                                                  | Loop Condition |
    | --------------------------------------------------------- | -------------- |
    | You want to find **exact index**                          | `while l <= r` |
    | You want to **narrow** to one point (like min/first/last) | `while l < r`  |
 ```

💡 Sliding window:
```
- The sliding window only works when all elements are non-negative, like in problems such as Minimum Size Subarray Sum.
-
| Condition      | Meaning                                  | Window Adjustment Logic                           |
| -------------- | ---------------------------------------- | ------------------------------------------------- |
| **At Most K**  | You can have **≤ K** distinct characters | Shrink window only when distinct chars **> K**    |
| **At Least K** | You need **≥ K** distinct characters     | Shrink only when distinct chars **< K**           |
| **Exactly K**  | You need **== K** distinct characters    | Shrink when **> K**, and count only when **== K** |
```

💡 Arrays:
```
💡 **Performance Tip**

- ✅ Prefer `for val in arr` over `for i in range(len(arr))` → avoids indexing overhead.
- ✅ Use `min(a, b)` / `max(a, b)` instead of manual `if` checks → faster and cleaner.


💡 **Performance Tip**

- ✅ **Index-based append** (e.g., `arr[i] = x`) is **faster** when memory is pre-allocated because it directly writes to a known position.
- ⚠️ **`.append()` or `.push()`** is **slightly slower** due to internal checks and resizing, but it's **safer and more flexible**.

```

💡 BackTracking:
```
- In backtracking, if you modify a list and store it — always use `.copy()` to avoid mutation bugs.
- 🔐 If something is mutable (like a list), it’s not hashable.
     Use immutable structures (like tuple) to store them in hash-based collections like sets and dictionaries.
- Sorting is mandatory to catch duplicates in adjacent
- 🔸 Backtracking by itself:
      ✔️ TC = O(choices^depth)
      ✔️ SC = O(depth) ← only recursion
      
      🔸 Backtracking generating all outputs:
      ✔️ TC = O(number_of_results × length_of_each_result)
      ✔️ SC = same as TC (if storing all results)
```

💡 Trees:
```
- Treat if not root: as a required safety seatbelt for all tree problems 🚗🌲 — not just for correctness, but to prevent your code from crashing outright.
-  ✅ pop() → "Now it's your turn to be processed"
   ✅ append() → "Get in line! I’ll process you later"
   ✅ This continues until all nodes are visited (in BFS style: left to right, level by level)

```
