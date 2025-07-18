
````markdown
==================================================================
🧩 Problem: Sudoku Solver
🔗 Link    : https://leetcode.com/problems/sudoku-solver/
📚 Topic   : Backtracking, Constraint Propagation, Sets
📈 Level   : Hard
==================================================================

📄 Description:
Write a program to solve a 9x9 Sudoku puzzle by filling the empty cells ('.') such that each row, each column, and each 3x3 sub-box contains the digits 1-9 without repetition.

---

## ✅ Brute-force:

my initial idea is:
    - pick one number add it and check whether it is valid number or not.
    - if not valid remove it (backtrack)

i got stuck with bruteforce:
    - selected one number but how to mark that number's overall row and column.

fix:
    - after some failed thoughts. i came to idea to take help of SET.
            - take list of 9 sets as row and same for column because soduku is of 9*9. also for grid we have another approach. discuss it in dry run
            - if one number selected store that num in first index of row and column and grid.simply we got list of 9 sets which has unique numbers.
    - rows -> [() , () , () , ...... ] same for columns and grids. hence we can access it with indexes

grid -->    0 1 2   --> 3*3 grid.
          0 - - -
          1 - - -
          2 - - -

        00 01 02
        10 11 12    so to get position of (5,7) of whole soduku in 3*3 grid --> use row -> row//3 , column -> col//3. (because of 3*3 grid)
        20 21 22


                                0   1   2   3   4   5   6   7   8
                        ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
                    0   │00 │01 │02 │**03 │04 │05**│06 │07 │08 │
                    1   │10 │11 │12 │**13 │14 │15**│16 │17 │18 │
                    2   │20 │21 │22 │**23 │24 │25**│26 │27 │28 │
                        ├───┼───┼───┼───┼───┼───┼───┼───┼───┤
                    3   │30 │31 │32 │**33 │34 │35**│36 │37 │38 │
                    4   │40 │41 │42 │**43 │44 │45**│46 │47 │48 │
                    5   │50 │51 │52 │**53 │54 │55**│56 │57 │58 │
                        ├───┼───┼───┼───┼───┼───┼───┼───┼───┤
                    6   │60 │61 │62 │**63 │64 │65**│66 │67 │68 │
                    7   │70 │71 │72 │**73 │74 │75**│76 │77 │78 │
                    8   │80 │81 │82 │**83 │84 │85**│86 │87 │88 │
                        └───┴───┴───┴───┴───┴───┴───┴───┴───┘


### 🔧 Code:
```python
def isvalid(row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    r = (row // 3) * 3
    c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] == num:
                return False
    return True

def backtrack(row, col):
    if row == 9:
        return True
    if col == 9:
        return backtrack(row + 1, 0)
    if board[row][col] != ".":
        return backtrack(row, col + 1)
    
    for num in map(str, range(1, 10)):
        if isvalid(row, col, num):
            board[row][col] = num
            if backtrack(row, col + 1):
                return True
            board[row][col] = "."
    return False

backtrack(0, 0)
```

---

### 🧠 Dry Run (simplified):

Input:
```
[["5","3",".",...],
 ["6",".",".",...],
 ...
]
```

→ Start from cell [0][2]  
→ Try "1" to "9", validate  
→ If valid → place → recurse  
→ If stuck, backtrack → try next number

---

## 🛑 Mistakes I Faced:

| ❌ Mistake                            | ✅ Fix                                                   |
|--------------------------------------|----------------------------------------------------------|
| Tried `board[row//3][col//3]`        | Invalid — doesn't access the 3x3 box                     |
| Mixed int and str (`int(num)` vs `"5"`) | Always work with strings when comparing Sudoku cells    |
| Used `if num in rows` instead of `rows[i]` | Remember: `rows`, `cols`, `boxes` are list of sets     |
| Redundant call to `backtrack(row, col-1)` | Unnecessary — backtracking is handled via recursion     |

---

## 🚀 Optimized Using Sets

Instead of checking entire rows/cols/boxes each time, **track used digits in sets**.

### 🔧 Code:
```python
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

# Pre-fill sets from board
for i in range(9):
    for j in range(9):
        if board[i][j] != ".":
            val = board[i][j]
            box = (i // 3) * 3 + (j // 3)
            rows[i].add(val)
            cols[j].add(val)
            boxes[box].add(val)

def backtrack(row, col):
    if row == 9:
        return True
    if col == 9:
        return backtrack(row + 1, 0)
    if board[row][col] != ".":
        return backtrack(row, col + 1)

    box = (row // 3) * 3 + (col // 3)
    for num in map(str, range(1, 10)):
        if num not in rows[row] and num not in cols[col] and num not in boxes[box]:
            board[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            boxes[box].add(num)

            if backtrack(row, col + 1):
                return True

            board[row][col] = "."
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[box].remove(num)

    return False

backtrack(0, 0)
```

---

## 🔍 Key Insight:

* Use `box = (i//3)*3 + j//3` to map 3x3 grid to a flat index (0–8)
* Instead of checking validity by scanning, use `set` lookups (`O(1)`)
* Backtracking = **choose → recurse → un-choose**

---

## ❓ Confusions Cleared

| Confusion                                 | Resolution                                          |
|------------------------------------------|-----------------------------------------------------|
| Can we access sets in list by index?     | ✅ Yes — just use `sets[i]`                         |
| Why use `str(num)` in sets?              | Board stores strings, not integers                 |
| Can we get 3x3 grid by `board[i//3][j//3]`? | ❌ No — that gets top-left of subgrid, not all cells |
| Is `chr(num + ord('0'))` better?         | Not needed — just use `str(num)`                   |

---

## 💡 What I Learned:

- Backtracking is natural for grid filling.
- Use `sets` to avoid repetitive scanning.
- Grid math matters: 3x3 box index is **row//3 \* 3 + col//3**
- **Dry runs** and debugging types (`str` vs `int`) is 🔑
- Avoid redundant recursions like `backtrack(row, col-1)`

---

## 📌 Summary

| Approach            | Time Complexity | Space Complexity | Notes                                |
|---------------------|------------------|------------------|--------------------------------------|
| Brute-force         | Exponential      | Recursive Stack   | Checks row/col/box each time         |
| Optimized with Sets | Exponential      | O(1) extra sets   | Fast constraint propagation          |

---
````
