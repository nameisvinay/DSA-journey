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

