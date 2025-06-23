---

````md
==================================================================
🧩 Problem: Longest Substring Without Repeating Characters
🔗 Link    : https://leetcode.com/problems/longest-substring-without-repeating-characters/
📚 Topic   : Sliding Window / HashSet
📈 Level   : Medium
==================================================================

## ✅ Problem Statement
Given a string `s`, find the length of the longest substring **without repeating characters**.

---

## 🔍 Intuition & Approach

I wanted to maintain a window with **unique characters**. The idea is to expand the window (`end`) as long as characters are not repeated. But when a duplicate is found, shrink the window from the start (`start`) until the duplicate character is removed.

### 🧠 Thought Process:
- Use a **Set** to store current window's characters.
- Maintain two pointers: `start` and `end`.
- For every character at `end`:
  - If it's **not in the set**, add it and move forward.
  - If it's **in the set**, remove from the start until duplicate is gone.
- Keep tracking the **max length**.

---

## 🔁 Dry Run (Example: `"abcabcbb"`)

```txt
start = 0, end = 0, seen = {}
- Add 'a', max = 1
- Add 'b', max = 2
- Add 'c', max = 3
- 'a' repeated → remove 'a', start = 1
- Add 'a', max = 3
- 'b' repeated → remove 'b', start = 2
- Add 'b', max = 3
...
Final max length = 3 ("abc")
````

---

## 🧪 Mistake I Made Initially

At first, I forgot to update `max_length` **after the loop ends**. That caused incorrect output for inputs where the last substring was the longest.

```python
# Forgot this:
max_length = max(max_length, end - start)
```

---

## ✅ Final Code (My Version)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        end = 0
        max_length = 0

        while end < len(s):
            while s[end] in seen:
                max_length = max(max_length, end - start)
                seen.remove(s[start])
                start += 1
            else:
                seen.add(s[end])
            end += 1

        max_length = max(max_length, end - start)  # Final update
        return max_length
```

---

## 🧾 Key Learnings

* Set helps maintain uniqueness in O(1) lookup.
* Sliding window is perfect for this kind of problem.
* Always ensure to update your result **after** loop ends.
* There are multiple ways to slide the window — both eager and lazy updates work, depending on where you check `max_length`.

---
