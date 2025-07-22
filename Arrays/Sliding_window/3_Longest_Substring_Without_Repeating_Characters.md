
````md
==================================================================
🧩 Problem: Longest Substring Without Repeating Characters
🔗 Link    : https://leetcode.com/problems/longest-substring-without-repeating-characters/
📚 Topic   : Sliding Window / HashSet
📈 Level   : Medium
==================================================================

## ✅ Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters**.

---

## 🔍 Intuition & Approach

I wanted to maintain a window with **unique characters**. The idea is to expand the window (`end`) as long as characters are not repeated. But when a duplicate is found, shrink the window from the start (`start`) until the duplicate character is removed.

### 🧠 Thought Process:
- Use a Set to store current window's characters.
- Maintain two pointers: `start` and `end`.
- For every character at `end`:
  - If it's not in the set**, add it and move forward.
  - If it's in the set**, remove from the start until duplicate is gone.
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

At first, I forgot to update `max_length` after the loop ends. That caused incorrect output for inputs where the last substring was the longest.

```python
# Forgot this:
max_length = max(max_length, end - start)
```

---

## ✅ Final Code (My Version)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        end = 0
        hs = set()
        while end<len(s):
            if s[end] not in hs:
                hs.add(s[end])
                end += 1
            else:
                hs.remove(s[start])
                start += 1
            max_length = max(max_length , end-start)
        return max_length
```

---

## 🧾 Key Learnings

* Set helps maintain uniqueness in O(1) lookup.
* Sliding window is perfect for this kind of problem.
* Always ensure to update your result **after** loop ends.
* There are multiple ways to slide the window — both eager and lazy updates work, depending on where you check `max_length`.

---
```
🧠 Time & Space Complexity
        Time Complexity: O(n)
              Each character is visited at most twice (once by end, once by start).
        
        Space Complexity: O(min(n, m))
              Where n is the length of the string
                    m is the size of the character set.

        For example:
              If input has lowercase letters only: O(26)
              If ASCII: O(128)
              If Unicode: can be more.
```
