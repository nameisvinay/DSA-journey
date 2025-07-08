```md
==================================================================
🧩 Problem: Permutations (Brute-Force Iterative Insertion)
🔗 Link    : https://leetcode.com/problems/permutations/
📚 Topic   : Backtracking, Arrays, Permutations, Recursion
📈 Level   : Medium
==================================================================

📄 Description:
Given an array `nums` of distinct integers, return all possible permutations of the numbers.  
Do **not use recursion** — use **iterative brute-force logic**.

---

## ✅ My Initial Brute Force Idea (Took ~3 hours to fully understand slicing-based insertion)

At first, I tried to simulate permutations using loops.  
My logic was to fix one number and loop over the rest — it worked for 2 elements, but broke with 3+ elements.

### Attempt 1 (didn't scale):
```python
for i in range(len(nums)):
    subset = [nums[i]]
    for j in range(len(nums)):
        if i != j:
            subset.append(nums[j])
    result.append(subset)
```

This only worked for 2 elements. For 3+, it repeated values or missed combinations.  
I then tried 3 nested loops and hardcoded combinations — but that’s not scalable.

---

## 🧠 Breakthrough: Insert at All Positions

Eventually, I learned a new technique:

> For each number in `nums`, insert it at **every possible position** inside every existing permutation.

We start with an empty permutation: `res = [[]]`.  
Then, for every new number, we **build new permutations** by inserting it at every index of each current permutation.

This unlocked everything 🔓

---

## 🔁 Final Working Code (Iterative)

```python
def permute(nums):
    res = [[]]  # Start with one empty permutation

    for num in nums:
        new_res = []
        for perm in res:
            for i in range(len(perm) + 1):  # insert num at every position
                new_perm = perm[:i] + [num] + perm[i:]
                new_res.append(new_perm)
        res = new_res  # update result

    return res
```

---

## 🧪 Dry Run (nums = [1, 2, 3])

Initial:  
`res = [[]]`

### Step 1: Add 1  
Insert into `[]` → `[1]`  
`res = [[1]]`

---

### Step 2: Add 2  
Insert into `[1]`:
- at index 0 → `[2, 1]`
- at index 1 → `[1, 2]`

`res = [[2,1], [1,2]]`

---

### Step 3: Add 3  
Insert into `[2,1]`:
- index 0 → `[3,2,1]`
- index 1 → `[2,3,1]`
- index 2 → `[2,1,3]`

Insert into `[1,2]`:
- index 0 → `[3,1,2]`
- index 1 → `[1,3,2]`
- index 2 → `[1,2,3]`

✅ Final result:
```python
[[3,2,1], [2,3,1], [2,1,3],
 [3,1,2], [1,3,2], [1,2,3]]
```

---

## ❓ Confusing Part I Faced:

I originally wrote:

```python
perm[:i] + [num] + perm[i+1:]
```

❌ This skips elements, because `perm[i+1:]` **removes** the value at position `i`.

✅ Correct version:
```python
perm[:i] + [num] + perm[i:]
```
This properly **inserts** the value at position `i` without skipping any element.

---

## 🧠 Slicing Realization

Slicing in Python:

```python
perm = [1, 2, 3]
perm[:1] + [9] + perm[1:]  # inserts 9 at index 1
→ [1, 9, 2, 3]
```

> Important: `perm[:i]` and `perm[i:]` always return **lists**, so the `+` operation concatenates them correctly.

This small change took me over 2 hours to digest — but once I got it, everything became easy.

---

## 📌 Summary of Steps

| Step | Num Inserted | Resulting Permutations             |
|------|---------------|------------------------------------|
| 1    | 1             | `[1]`                              |
| 2    | 2             | `[2,1], [1,2]`                     |
| 3    | 3             | `[3,2,1], [2,3,1], [2,1,3]`, <br>`[3,1,2], [1,3,2], [1,2,3]` |

---

## 💡 What I Learned

- Brute-force permutations can be done **without recursion** using **insertion logic**.
- **Slicing is powerful**: `perm[:i] + [num] + perm[i:]` is the key.
- Start with one empty permutation and grow step by step.
- Take your time — 3 hours on one problem gave me deep clarity.

---

## 🧠 Bonus Tip:

> This approach is the base for recursive DFS/backtracking too — you’re just controlling the insertions with a recursive stack instead of a loop.

---

✅ I now fully understand iterative permutation generation and slicing. Next up, I’ll explore the **recursive backtracking** version too!


```
## 🔄 Recursive Backtracking (Final Working Solution)

This recursive idea is clean:

1. Start from index `fi = 0`.
2. Swap each index with `fi`.
3. Recurse for `fi + 1`.
4. Backtrack (undo the swap).
5. When `fi == len(nums) - 1`, it means one full permutation is ready.

```python
def permute(nums):
    def backtrack(fi):
        if fi == len(nums) - 1:
            result.append(nums.copy())  # ✅ safe copy
            return
        for i in range(fi, len(nums)):
            nums[i], nums[fi] = nums[fi], nums[i]   # swap
            backtrack(fi + 1)                        # recurse
            nums[i], nums[fi] = nums[fi], nums[i]   # backtrack

    result = []
    backtrack(0)
    return result
```

---

## 🧠 Dry Run for nums = [1, 2, 3]

```text
Level 0 (fi = 0): [1, 2, 3]
    ↳ Swap i=0, fi=0 → [1, 2, 3]
        Level 1 (fi = 1):
            ↳ Swap i=1, fi=1 → [1, 2, 3]
                Level 2 (fi = 2): ✅ Append [1,2,3]
            ↳ Backtrack → [1, 2, 3]
            ↳ Swap i=2, fi=1 → [1, 3, 2]
                Level 2 (fi = 2): ✅ Append [1,3,2]
            ↳ Backtrack → [1, 2, 3]
    ↳ Swap i=1, fi=0 → [2, 1, 3]
        ... and so on
```

---

## ❌ Common Mistake I Made:

```python
result.append(nums)  # ❌ WRONG
```
- This appends the **reference** to nums.
- So all entries in `result` will point to the **same list**, which gets mutated on future swaps.

✅ Fix:
```python
result.append(nums.copy())  # snapshot
```
Or use:
- `result.append(nums[:])`
- `result.append(list(nums))`

---

## 🔍 Visualizing the Problem:

Think of recursion as a tree:
```
            []
      /     |     \
   [1]    [2]    [3]
   / \     / \    / \
[1,2][1,3] ... etc
```
Every level adds one more number, exploring all positions by swapping.

---

## 💡 What I Learned:

- Backtracking is just trying all options and undoing afterward.
- **`.copy()` is crucial** to preserve valid results at the moment they are complete.
- Recursion works cleanly if base + recursive + backtrack are in sync.
- Brute force with loops is okay for understanding but not scalable.

---

> ✅ **Golden Rule:**
> In backtracking, if you modify a list and store it — always use `.copy()` to avoid mutation bugs.

---

## ✅ Output Example:
```python
Input : [1,2,3]
Output:
[
  [1,2,3], [1,3,2],
  [2,1,3], [2,3,1],
  [3,1,2], [3,2,1]
]
```
````
