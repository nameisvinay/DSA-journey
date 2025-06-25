
````md
==================================================================
🧩 Problem: Longest Repeating Character Replacement
🔗 Link    : https://leetcode.com/problems/longest-repeating-character-replacement/
📚 Topic   : Sliding Window, Hashing
📈 Level   : Medium
==================================================================

📄 Description:
----------------
Given a string `s` and an integer `k`, you can replace at most `k` characters in `s` 
so that the resulting substring contains only one distinct character.

Return the **length of the longest possible substring** you can get after performing at most `k` replacements.

---

🧠 Intuition:
--------------
We want a **window** where the **majority character** remains and all others (non-majority) 
can be **replaced** — as long as the number of replacements needed is `<= k`.

🔑 Key Insight:
To make all characters in a window the same, we can:
→ Keep the most frequent character unchanged  
→ Replace the rest  
→ Total replacements needed = `(window size - max frequency in window)`

---

🚧 My Initial Code (Buggy):
----------------------------
```python
seen = {}
start = 0
end = 0
max_length = 0

while end < len(s):
    seen[s[end]] = seen.get(s[end], 0) + 1
    max_freq = max(val for val in seen.values())  # ✅ correct logic, but recomputed each time

    window_size = end - start + 1

    if window_size - max_freq <= k:
        max_length = max(max_length, window_size - max_freq)  # ❌ wrong - should store full window size

    while window_size - max_freq == k:  # ❌ stale window_size
        seen[s[start]] -= 1
        start += 1

    end += 1

return max_length
````

### 🔍 Mistakes:

* ❌ Stored `window_size - max_freq` in `max_length` instead of full window size
* ❌ Shrink condition was incorrect and based on stale `window_size`
* ❌ Constant recomputation of `max(seen.values())`

---

## ✅ Final Working Code (Optimized Version):

```python
def characterReplacement(s: str, k: int) -> int:
    seen = {}
    start = 0
    end = 0
    max_length = 0
    max_freq = 0

    while end < len(s):
        seen[s[end]] = seen.get(s[end], 0) + 1
        max_freq = max(max_freq, seen[s[end]])  # ✅ update only when end moves

        window_size = end - start + 1

        if window_size - max_freq <= k:
            max_length = max(max_length, window_size)

        while (end - start + 1) - max_freq > k:
            seen[s[start]] -= 1
            start += 1

        end += 1

    return max_length
```

---

## 🧪 Example:

```python
s = "AABABBA"
k = 1
```

✅ Output: `4`

Explanation: Replace 1 'B' → `"AABA"` → 4 characters same → ✅

---

## 🧠 Why `max_freq = max(max_freq, seen[s[end]])` works:

* We only increase `max_freq` when frequency increases
* Even if `max_freq` becomes stale during shrinking, it's okay
* If the window becomes invalid (`too many replacements`), it shrinks automatically

So correctness is **preserved**, and **performance improves**.

---

## ⏱ Time and Space Complexity:

| Metric   | Value                                  |
| -------- | -------------------------------------- |
| 🕒 Time  | `O(N)` (one pass over string)          |
| 💾 Space | `O(1)` (at most 26 chars in seen dict) |

---

## 📌 Summary of What I Learned:

* The trick is in tracking **max frequency** in a sliding window
* If `(window size - max freq) <= k`, we have a valid window
* Optimization: `max_freq` can be tracked without recomputing `max()` every time
* Sliding window can grow/shrink dynamically to maintain a valid condition
* Never store "replacements" as the result — always store window size

---

## 💡 Interview Tip:

Explain the core check:

> "**To make all characters the same in a window, we just need to replace the rest — so if the number of non-majority chars ≤ k, it's valid.**"

---
