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

**🧠 Core Idea:**
Use two pointers (`start`, `end`) and a frequency map to track how many characters are still needed.
Shrink the window only **when all required chars are covered** (i.e., all `freq.values() <= 0`).
Update the minimum window during that time.

---

### ✅ One-Line Takeaway:

> Move `end` to build a valid window, then move `start` to shrink the window **as long as it's valid**, and track the smallest length.
> Takeaway: When the window is valid (all freq ≤ 0), try to shrink it by moving start. Watch when freq becomes positive again.

---

### 🔁 Window Movement Logic (Tracked for Revision):

* **Start expanding:**
  Slide `end` and reduce `freq[s[end]]` if it's a required char.

* **When window is valid:**
  All values in `freq` ≤ 0 → means current window has all required chars.

* **Now try to shrink:**
  Move `start` forward **while still valid**.
  If `freq[s[start]]` increases above 0, break.
  Before breaking, update `min_len` and `start_idx`.

---

### ❗ Points Where I Got Stuck (Self-reflection):

1. ✅ I didn't know **how to handle logic after shrinking the window**.

   > 🔸 *Note: After increasing `start`, just break the loop and continue expanding `end`.*

2. ❓ I was unsure if I should keep moving `start` until `end` again.

   > 🔸 *Note: No. After one invalidation (any freq > 0), stop shrinking.*

3. ⚠️ I forgot the condition to **move `start` only if the window is still valid**.

   > 🔸 *Note: Only move `start` while `freq.values() <= 0`.*

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

## ✅ CP Style Version (Array-Based Optimized) - Faster than hash based approach

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

            mp[ord(s[start])] += 1
            if mp[ord(s[start])] > 0:
                count += 1
            start += 1
        end += 1

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

## ✅ What I Learned:

* Sliding window + frequency map is the key to optimal substring problems.
* Use `val <= 0` to handle extra matches.
* Track exact start index of the minimal valid window.


* Hashmap version is preferred for readability and flexibility.
* ASCII array version is faster for contests but less general.

---

* after 10days my stucking points:

        **🔍 Personal Thought While Solving:**
        
        ❓ *My idea:*
        
        > After breaking out of the valid window (when `freq[s[start]] > 0`),
        > **Should I just keep moving `start` toward `end`** while increasing the frequencies?
        
        🟡 But here's the **realization**:
        No — once the window is invalid (missing a required character),
        🔸 We should **stop moving `start`**,
        🔸 And instead **resume expanding `end`**
        until we again include the missing character(s) and form a valid window.
        
        📌 In short:
        
        > ❌ Don't move `start` blindly.
        > ✅ After breaking, only `end` should move until the window becomes valid again.
        
        ❓ Doubt:
        Should I move the end pointer continuously until all freq values are ≤ 0?
        Or should I check the window validity at each step as I move end?


Another approach:

- if we find s[end] in freq then decrement count.
- when count becomes equals to 0. shrink from front.
- if freq[s[start]] starts grows when it moves to above 0 then increment count.
---
