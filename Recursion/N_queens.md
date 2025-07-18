
---

# 🧠 Leetcode 51. N-Queens — DSA Notes

## 🧾 Problem Statement

Place `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all possible board configurations.

Each solution must be a list of strings where:

* `'Q'` represents a queen
* `'.'` represents an empty cell

---

## 🌟 Intuition

The problem is classic **backtracking**:

* Place a queen row by row.
* At each step, try placing a queen in each column.
* Before placing, check if it's **safe** (i.e., doesn't attack any previous queen).
* If safe, place it and proceed to the next row.
* If a configuration reaches `row == n`, it's a valid solution.
* Use backtracking to explore all configurations.

We can solve this via:

1. ✅ **Brute-force backtracking with manual validity check**
2. ✅ **Optimized version using boolean arrays (`cols`, `ld`, `rd`)**

---

## 🔨 Brute-force Implementation

```python
def solveNQueens(n):
    def isvalid(row, col):
        for r, c in queen:
            if row == r or col == c or row - col == r - c or row + col == r + c:
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append(board.copy())
            return

        for col in range(n):
            if isvalid(row, col):
                queen.append((row, col))
                board.append("." * col + "Q" + "." * (n - col - 1))
                backtrack(row + 1)
                queen.pop()
                board.pop()

    result = []
    board = []
    queen = []
    backtrack(0)
    return result
```

### 🔍 Dry Run (n = 4)

Try placing queens row by row:

* row = 0 → try all columns → choose col = 1
* row = 1 → try columns, skip unsafe → choose col = 3
* row = 2 → invalid positions
* Backtrack → undo and try new column in row = 1

... continues until all possibilities explored.

---

## ✅ Optimized Version — Using Booleans

We use:

* `cols[col]` → column attack
* `ld[row-col+n]` → left diagonal attack
* `rd[row+col]` → right diagonal attack

```python
def solveNQueens(n):
    cols = [False] * n
    ld = [False] * (2 * n)
    rd = [False] * (2 * n)

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if cols[col] or ld[row - col + n] or rd[row + col]:
                continue

            board[row][col] = "Q"
            cols[col] = ld[row - col + n] = rd[row + col] = True

            backtrack(row + 1)

            cols[col] = ld[row - col + n] = rd[row + col] = False
            board[row][col] = "."

    result = []
    board = [["."] * n for _ in range(n)]
    backtrack(0)
    return result
```

---

## 🤔 Confusion Points

### 🔹 1. Why `row-col+n` in left diagonal?

Left diagonals have same value for `row - col`. This could be **negative**, so we shift by `+n` to make index non-negative.

### 🔹 2. Why store board using `"".join(r)`?

The final output format expects:

```python
[".Q..", "...Q", "Q...", "..Q."]
```

So we convert internal 2D board (list of lists) using:

```python
["".join(r) for r in board]
```

### 🔹 3. Board Initialization

```python
board = [["."] * n for _ in range(n)]
```

Each row is a list of dots. We place `"Q"` when we choose that cell.

### 🔹 4. Why check `if cols[col] or ld[...] or rd[...]`?

Because:

* If any of these is `True`, that means a queen is **already** attacking that column/diagonal.
* Hence we skip that position and continue to the next column.

---

## 🧠 Learnings

* 🔁 Backtracking needs clean recursion with proper **undo (pop/remove/reset)** steps.
* ⛔ Don't forget to **restore** the state after recursion — classic mistake.
* ✅ Optimization with arrays (`cols`, `ld`, `rd`) speeds up significantly vs brute force.
* 📌 `["".join(row) for row in board]` is clean way to get required output format.

---

## ✅ Summary

| Approach       | Time  | Space | Notes                         |
| -------------- | ----- | ----- | ----------------------------- |
| Brute-force    | O(N!) | O(N²) | Manual conflict checking      |
| Optimized Bool | O(N!) | O(N²) | Fast using pre-checked arrays |

* Both approaches explore `N!` configurations.
* Optimized one avoids redundant checks, reducing overhead significantly.

---
