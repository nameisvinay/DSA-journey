```md
=============================================================
# 🧩 Problem: Minimum Window Substring

🔗 [Leetcode 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
📚 Topic: Sliding Window, Hashing
📈 Level: Hard
==============================================================


## 📄 Description:

Given two strings `s` and `t`, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.
If no such window exists, return an empty string `""`.


## ✅ Constraints:

* Strings `s` and `t` consist of English letters.
* You must find the smallest substring in `s` that contains all characters of `t` **with the correct frequency**.

````

## 🧠 My Thought Process:

### ✔️ Initial Idea:

* Use a frequency dictionary `seen` to store how many of each character are needed from `t`.
* Slide a window over `s` using two pointers `start` and `end`.
* When a required character is found, decrement its count in `seen`.
* When the window has all required characters (i.e., all values in `seen` are `<= 0`), try to shrink it to minimize length.
* Track `min_length` and `min_start` to return the final substring.

---

## ❌ Bugs I Faced and Fixed:

### 🔸 Mistake 1:

Used:

```python
while all(val == 0 for val in seen.values()):
```

This failed for extra characters (e.g., more A’s than needed), since some values became `-1`.

### ✅ Fix:

```python
while all(val <= 0 for val in seen.values()):
```

This ensures all required chars are matched (and maybe more, which is still valid).

---

### 🔸 Mistake 2:

Used:

```python
return s[start:start + min_length]
```

But `start` had moved forward during shrinking.

### ✅ Fix:

Track `min_start` when `min_length` is updated:

```python
min_start = start
```

Return using `min_start`:

```python
return s[min_start:min_start + min_length]
```

---

## ✅ Final Working Code (Hashmap-Based)

```python
def minWindow(s: str, t: str) -> str:
    min_length = float('inf')
    min_start = 0

    seen = {}
    for i in t:
        seen[i] = seen.get(i, 0) + 1

    start = 0
    end = 0
    while end < len(s):
        if s[end] in seen:
            seen[s[end]] -= 1

        # Valid window check — all values should be <= 0
        while all(val <= 0 for val in seen.values()):
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start
            if s[start] in seen:
                seen[s[start]] += 1
            start += 1

        end += 1

    return "" if min_length == float('inf') else s[min_start:min_start + min_length]
```

---

## ✅ CP Style Version (Array-Based Optimized)

### 🧠 Logic:

* Use a fixed-size ASCII array `mp[256]` to store frequency of characters in `t`.
* Decrement `count` whenever a required character is matched.
* Once `count == 0`, we have a valid window. Try to shrink from the left.

### ⚡️ Code:

```python
def minWindow(s: str, t: str) -> str:
    start = end = 0
    start_idx = 0
    min_len = float('inf')
    mp = [0] * 256
    count = len(t)

    for char in t:
        mp[ord(char)] += 1

    while end < len(s):
        if mp[ord(s[end])] > 0:
            count -= 1
        mp[ord(s[end])] -= 1
        end += 1

        while count == 0:
            if min_len > end - start:
                min_len = end - start
                start_idx = start

            if mp[ord(s[start])] == 0:
                count += 1
            mp[ord(s[start])] += 1
            start += 1

    return "" if min_len == float('inf') else s[start_idx:start_idx + min_len]
```

---

## 🧪 Example:

```python
s = "ADOBECODEBANC"
t = "ABC"
```

✅ Output: `"BANC"`

---

## ⏱ Time and Space Complexity

| Complexity | Value                                               |
| ---------- | --------------------------------------------------- |
| 🕒 Time    | `O(N)` – Each character is visited at most twice    |
| 💾 Space   | `O(K)` for hashmap version, `O(256)` for CP version |

---

## 🆚 My Version vs Instructor's Version

| Feature                        | My Version (`dict`, `<=0`)         | Instructor’s Version (`mp[256]`)      |
| ------------------------------ | ---------------------------------- | ------------------------------------- |
| **Data structure**             | `dict` / `Counter`                 | Fixed-size `int[256]` array           |
| **Character handling**         | Works with any character (Unicode) | Works best only with ASCII (0–255)    |
| **Readability**                | Easier to read & debug             | Bit harder, less intuitive            |
| **Efficiency (constant-wise)** | Slightly slower due to hashing     | Slightly faster due to array indexing |
| **Flexibility**                | Works for all scripts/languages    | Breaks for non-ASCII chars            |
| **Interview suitability**      | ✅ Preferred in interviews          | ⚠️ More common in contests/CP         |

---

## ✅ What I Learned:

* Sliding window + frequency map is the key to optimal substring problems.
* Use `val <= 0` to handle extra matches.
* Track exact start index of the minimal valid window.
* Hashmap version is preferred for readability and flexibility.
* ASCII array version is faster for contests but less general.

---
