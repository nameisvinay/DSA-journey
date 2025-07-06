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

## ❓ Confusing Part I Faced:

I was stuck on why we do `+k - 1` and then `+1`.

> 🧠 Explanation:
> - We do `+k-1` because counting starts from the **current person**.
> - We add `+1` at the end to convert from **0-based to 1-based** answer.

That made everything clear.

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

---

## 💡 What I Learned:

- Simulation is helpful for understanding, but recursive and iterative logic is **optimal and cleaner**.
- Indexing adjustments (`+k-1` and `+1`) need **careful tracking**.
- Bottom-up iteration avoids recursion stack and is just as powerful.
- Recursive gives intuition, iterative gives clarity.

---
