
```md
==================================================================
🧩 Problem: Josephus Problem
🔗 Link    : https://leetcode.com/problems/find-the-winner-of-the-circular-game/  
📚 Topic   : Recursion, Math, Simulation
📈 Level   : Medium
==================================================================

📄 Description:
There are `n` friends in a circle, numbered from 1 to n. Starting from person 1, every `k-th` person is eliminated in the circle until only one person remains. Return the number of the winner.

This is the classic **Josephus Problem**.

---

## ✅ My Understanding:

I imagined people sitting in a circle. I started with a brute-force idea where I keep a list and remove every k-th person by looping.  
But then I found a **recursive pattern** where instead of simulating every round, we can use a recurrence relation to find the winner.

---

## 🧠 Key Idea (Recursive Intuition):

Let’s define `f(n, k)` as the position (0-based) of the winner for `n` people and eliminating every `k-th`.

**Base Case:**
- If there’s only one person, they are the winner: `f(1, k) = 0`

**Recursive Relation:**
- `f(n, k) = (f(n - 1, k) + k) % n`

This means:  
→ Solve for `n-1`, and then adjust the winner's position by `k`, modulo `n`.

In the end, convert this 0-based result to 1-based by adding 1.

---

## 🚀 Initial Brute-force Attempt (My First Thought):

```python
def josephus_brute(n, k):
    people = list(range(1, n + 1))
    idx = 0

    while len(people) > 1:
        idx = (idx + k - 1) % len(people)
        people.pop(idx)

    return people[0]
```

**❌ Time:** O(nk) — gets slow for large n.  
But helped me understand the process clearly.

---

## ✅ Final Recursive Code:

```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n, k):
            if n == 1:
                return 0
            return (josephus(n - 1, k) + k) % n
        
        return josephus(n, k) + 1  # convert to 1-based index
```

---

## 🔄 Dry Run (n=5, k=3):

People: [1, 2, 3, 4, 5]  
Eliminations:  
- 3 → [1, 2, 4, 5]  
- 1 → [2, 4, 5]  
- 5 → [2, 4]  
- 2 → [4] ✅ Winner

In recursion:

```
josephus(1, 3) = 0
josephus(2, 3) = (0 + 3) % 2 = 1
josephus(3, 3) = (1 + 3) % 3 = 1
josephus(4, 3) = (1 + 3) % 4 = 0
josephus(5, 3) = (0 + 3) % 5 = 3 → +1 = 4 (1-based)
```

Winner = 4 ✅

---

## 🧠 Iterative Version:

```python
def josephus_iterative(n, k):
    res = 0
    for i in range(2, n + 1):
        res = (res + k) % i
    return res + 1  # convert to 1-based
```

We start from 2 because base case for 1 is known (position 0). Each iteration simulates adding one more person to the circle.

---

## 💡 What I Learned:

- Josephus has a **clean recurrence relation** if seen as position-shifting.
- I understood how to **simulate manually first**, then convert into recursive math.
- Iterative method is compact and avoids stack overflow.
- The key is **shifting the result forward** by `k` and using modulo to wrap around.

---
