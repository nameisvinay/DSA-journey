
---

## 🔁 Group Anagrams — Summary (Leetcode - (https://leetcode.com/problems/group-anagrams/))

### ✅ **Approach 1: Hashmap + Sorted String (Tuple as Key)**

* Key Idea: **Anagrams have the same sorted characters**

**Steps:**

1. Loop through each word
2. Sort it → `tuple(sorted(word))` (we use **tuple** as it's hashable for dict key)
3. Use this tuple as the key in a hashmap (dictionary)
4. Append the original word to the list at that key
5. Finally return all the hashmap values

```py
{
  ('a','e','t'): ['eat', 'tea', 'ate'],
  ('a','n','t'): ['tan', 'nat'],
  ...
}
```

🟡 **Time Complexity**: O(n \* k log k)
(where `n` = number of words, `k` = avg length of word due to sorting)

---

### ✅ **Approach 2: Hashmap + Frequency Count (Faster)**

* Key Idea: Anagrams have **same letter frequency**

**Steps:**

1. For each word, create a **26-length frequency tuple**
   (1 for each alphabet: a to z)
2. Use this frequency tuple as the key in hashmap
3. Append word to the list at that key
4. Return all hashmap values

```py
{
  (1,0,0,...,1): ['eat', 'tea', 'ate'],
  (1,0,1,...,0): ['bat'],
  ...
}
```

🟢 **Time Complexity**: O(n \* k)
(no sorting; just count freq of `k` chars)

---

### 🧠 When to Use What?

| Method    | Speed  | Notes                        |
| --------- | ------ | ---------------------------- |
| Sorting   | Slower | Easier to write, but costly  |
| Frequency | Faster | Efficient for longer strings |

---
