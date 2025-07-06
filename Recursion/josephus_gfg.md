same technique but 0-indexed in leetcode - 1823. Find the Winner of the Circular Game


````markdown
==================================================================
🧩 Problem: Josephus Problem
🔗 Link    : https://leetcode.com/problems/find-the-winner-of-the-circular-game/
📚 Topic   : Recursion, Math, Simulation
📈 Level   : Medium
==================================================================

📄 Description:
There are `n` friends sitting in a circle, numbered from 1 to n. They start passing a token and every `k`-th friend gets eliminated. The circle shrinks until only one person remains. You need to return the **winner's number** (1-based index).

---

## ✅ My Initial Brute Force Idea (Took ~3hrs to reach recursion)

At first, I tried to **simulate** the process literally by rotating a list and eliminating every `k`-th person.

```python
def brute_force_josephus(n, k):
    people = list(range(1, n + 1))
    idx = 0

    while len(people) > 1:
        idx = (idx + k - 1) % len(people)
        people.pop(idx)

    return people[0]
```

Works fine for small `n`, but this is **O(n^2)** due to `pop()` in a list.

---

## 🔄 Iterative Version (Fast & Clean)

Then I found this clean iterative method:

```python
def josephus_iterative(n, k):
    res = 0
    for i in range(2, n + 1):
        res = (res + k) % i
    return res + 1  # 1-based indexing
```

---

## ⚖️ Small Difference I Observed:

| Aspect                     | Recursive                                   | Iterative                                     |
|----------------------------|---------------------------------------------|-----------------------------------------------|
| Indexing                   | Needs manual conversion to 1-based          | Add `+1` at the end of loop                   |
| Base Case                  | Defined for `n == 1`                        | Loop starts from `i = 2`                      |
| Expansion Direction        | Top-down (reduces `n` each call)            | Bottom-up (builds from `n = 2` to `n`)        |
| Traceability               | Feels more like mathematical recurrence     | Easier to understand and track computation    |

This helped me decide when to use each depending on the clarity I need.

---

## 🔍 Dry Run (Recursive)

```
n = 5, k = 3

Base:
f(1) = 0

josephus(4, 2)
↳ josephus(3, 2)
   ↳ josephus(2, 2)
      ↳ josephus(1, 2)
         ↳ returns 0   ← base case

then back up:
josephus(2, 2) = (0 + 2) % 2 = 0
josephus(3, 2) = (0 + 2) % 3 = 2
josephus(4, 2) = (2 + 2) % 4 = 0


josephus(1, 2) = 0

josephus(2, 2) = (0 + 2) % 2 = 0  
→ survivor at index 0 among 2 people

josephus(3, 2) = (0 + 2) % 3 = 2  
→ survivor at index 2 among 3 people

josephus(4, 2) = (2 + 2) % 4 = 0  
→ survivor at index 0 among 4 people

```

## 🧠 Recursive Formula (Classic Josephus)

I found the recursive formula from hints and tutorials:

- For 0-based indexing:  
  `f(n) = (f(n-1) + k) % n`
- Base case: `f(1) = 0`
- To convert to 1-based answer, we do:

```python
def findTheWinner(n, k):
    if n == 1:
        return 1
    return ((findTheWinner(n - 1, k) + k - 1) % n) + 1
```

---

1. **Go deep** until `n == 1`.
2. **Start solving on the way back** using the formula `(josephus(n-1, k) + k) % n`.



## ❓ Confusing Part I Faced:

I was stuck on why we do `+k - 1` and then `+1`.

> 🧠 Explanation:
> - We do `+k-1` because counting starts from the **current person**.
> - We add `+1` at the end to convert from **0-based to 1-based** answer.

That made everything clear.

---

## 💡 What I Learned:

- Simulation is helpful for understanding, but recursive and iterative logic is **optimal and cleaner**.
- Indexing adjustments (`+k-1` and `+1`) need **careful tracking**.
- Bottom-up iteration avoids recursion stack and is just as powerful.
- Recursive gives intuition, iterative gives clarity.

---

Yes buddy, **exactly!** 🎯

> 🔁 **In the recursive formula**:
>
> ```python
> josephus(n - 1, k) + k) % n
> ```
>
> 👉 The `k - 1` is **implicitly handled** by the recurrence logic — **you don’t need to subtract 1 manually.**

---

## ✅ Why `k - 1` is Not Needed in Recursion?

Because the recursion builds upon a **previous survivor's position** after one person is eliminated. Let’s break it down with an example:

---

### 🔍 Example: `n = 5, k = 3`

Let’s look at the final recursive form:

```python
josephus(5, 3)
= (josephus(4, 3) + 3) % 5
= ((josephus(3, 3) + 3) % 4 + 3) % 5
...
```

At every recursive step:

* We're **shifting the position of the survivor** by `+k`, and wrapping it around with `% n`.
* That shift already assumes **one person is eliminated** in the prior step, so we’re moving forward **by `k` positions** from the survivor of the reduced circle.

---

## 💬 In contrast (Iterative or Simulation):

We do:

```python
index = (index + k - 1) % len(people)
```

Here, we manually subtract 1 because:

* We're **eliminating** the `k-th` person, counting from the current index (which is `1-based`).
* So to get the correct index to remove, we subtract 1.

---

## 💡 Summary

| Approach               | Formula                         | Notes                            |
| ---------------------- | ------------------------------- | -------------------------------- |
| Recursive (0-based)    | `(josephus(n - 1, k) + k) % n`  | `k - 1` is implicitly handled    |
| Iterative / Simulation | `(index + k - 1) % len(people)` | `-1` needed to get correct index |
