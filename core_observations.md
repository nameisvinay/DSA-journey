###

```
  💡 Next greater:
   when we are looking for future elements (next greater), it's better to traverse from right to left(reversed).
```

```
  💡 subsets-II:
   len(res) actually gives us the index where we should start forming new subsets in the next step — especially when handling duplicates.
```

```
  💡 Binary search loop condition:
    | Use Case                                                  | Loop Condition |
    | --------------------------------------------------------- | -------------- |
    | You want to find **exact index**                          | `while l <= r` |
    | You want to **narrow** to one point (like min/first/last) | `while l < r`  |
 ```

```
| Condition      | Meaning                                  | Window Adjustment Logic                           |
| -------------- | ---------------------------------------- | ------------------------------------------------- |
| **At Most K**  | You can have **≤ K** distinct characters | Shrink window only when distinct chars **> K**    |
| **At Least K** | You need **≥ K** distinct characters     | Shrink only when distinct chars **< K**           |
| **Exactly K**  | You need **== K** distinct characters    | Shrink when **> K**, and count only when **== K** |
```
