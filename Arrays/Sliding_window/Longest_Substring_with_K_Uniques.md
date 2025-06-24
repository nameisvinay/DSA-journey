
````markdown
==================================================================
🧩 Problem: Longest Substring with At Most K Distinct Characters
📚 Topic   : Sliding Window
📈 Level   : Medium
==================================================================

📄 Description:
Given a string `s` and an integer `k`, return the length of the **longest substring** that contains **at most `k` distinct characters**.

If no such substring exists, return `-1`.

---

### 🚀 Approach

This is a classic **sliding window + hashmap** problem.  
We expand the `end` pointer to include new characters and shrink the `start` pointer when the number of distinct characters exceeds `k`.

---

### ✅ Key Points to Remember:

- Use a **hashmap** `seen` to keep count of each character in the current window.
- If `len(seen) > k`, shrink the window from the left until it's valid again.
- At each step, update the `max_length` only if the window is valid.
- If no valid substring is found, return `-1`.

---

### ⚠️ Mistake I Made Initially:

```python
# My earlier mistake:
if seen[s[start]] == 0:
    del seen[s[start]]
    start += 1
````

🔴 I was **deleting the next character** (`s[start+1]`) instead of the **current one**, which misaligned the window.

---

### ✅ Final Working Code:

```python
class Solution:
    def longestKSubstr(self, s, k):
        seen = {}
        max_length = -1
        start = 0
        end = 0
        
        while end < len(s):
            seen[s[end]] = seen.get(s[end], 0) + 1
            
            # Shrink window if distinct chars exceed k
            while len(seen) > k:
                seen[s[start]] -= 1
                if seen[s[start]] == 0:
                    del seen[s[start]]
                start += 1

            # Only update max_length when window is valid
            if len(seen) == k:
                max_length = max(max_length, end - start + 1)

            end += 1

        return max_length
```

---

### 🧠 Intuition:

* When window has **more than `k` distinct chars**, it's invalid → shrink it.
* When window has **exactly `k`**, update the max length.
* This sliding window ensures O(n) time and no repeated work.

---

### 🌟 Example:

Input: `s = "aabacbebebe"`, `k = 3`
Output: `7`
Explanation: `"cbebebe"` is the longest valid substring with 3 distinct characters.

---

### 🔁 Variants:

* Longest substring with **exactly k** distinct characters
* Longest substring with **at most k vowels**
* Longest substring with **k unique characters** with no repeating
```
  | Condition      | Meaning                                  | Window Adjustment Logic                           |
| -------------- | ---------------------------------------- | ------------------------------------------------- |
| **At Most K**  | You can have **≤ K** distinct characters | Shrink window only when distinct chars **> K**    |
| **At Least K** | You need **≥ K** distinct characters     | Shrink only when distinct chars **< K**           |
| **Exactly K**  | You need **== K** distinct characters    | Shrink when **> K**, and count only when **== K** |
```

---

📝 **Takeaway**:
This problem improves your grip on sliding window logic + hashmap usage, and builds a good base for more complex window variants.
