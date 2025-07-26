
---

## ✅ **Sudoku Backtracking – My Complete Notes**

---

### 🔨 **How I Solved It**

* Created 3 sets: `rows`, `cols`, `grid` — to track used numbers.
* Used formula: `box = (row // 3) * 3 + (col // 3)` to identify 3x3 grid.
* Prefilled the sets with existing numbers from the board.
* Wrote a `backtrack(row, col)` function to try filling empty cells.
* If cell already has a number → move to `col + 1`.
* If cell is `"."`, try numbers `1` to `9`.
* For each valid number (not in row/col/grid):

  * Place it on the board.
  * Add it to the sets.
  * Move to next column.
  * If that move leads to solution → return `True`.
* If not → backtrack:

  * Reset cell to `"."`.
  * Remove number from sets.
* If `col == 9`, move to next row (`row + 1`, `col = 0`).
* If `row == 9`, board is complete → return `True`.

---

### ⚠️ **Where I Got Stuck**

* ❌ Didn’t return `False` when none of the numbers worked in the loop.
* ❌ Forgot to stop at the first valid solution (when `row == 9`).
* ❌ Used `result.append(board.copy())` → which only shallow copied the board.
* ❌ Did `return result.append(...)` → but `append()` returns `None`.
* ❌ Thought I need to return or store board separately — but question asked **in-place**.

---

### 💡 **Things I Realized**

* ✅ I don’t need extra space (`result` list) if the board is modified in-place.
* ✅ Deep copy for 2D board = `[row[:] for row in board]`, not `board.copy()`.
* ✅ `return True` after placing the last valid number when board is done (`row == 9`).
* ✅ Always `return False` if none of the numbers worked — to trigger backtracking.
* ✅ Sudoku box index formula is important: `(row // 3) * 3 + (col // 3)`.

---

### 📌 **Things to Remember**

* ✔️ Return `True` when board is complete (`row == 9`).
* ✔️ Return `False` when no valid number fits — essential for backtracking.
* ✔️ Use in-place updates if question says “solve in-place”.
* ✔️ Deep copy when storing board: `[row[:] for row in board]`.
* ✔️ Don't use `return append(...)` — separate them.
* ✔️ For filled cells → skip with `backtrack(row, col + 1)`.

---
