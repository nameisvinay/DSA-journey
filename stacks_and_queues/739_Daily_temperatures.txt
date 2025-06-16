==================================================================
🧩 Problem: Daily Temperatures  
🔗 Link    : https://leetcode.com/problems/daily-temperatures/  
📚 Topic   : Stack (Monotonic Decreasing Stack)  
📈 Level   : Medium  
==================================================================

📄 Description:
Given a list of daily temperatures `T`, return a list `answer` such that `answer[i]` is the number of days 
you have to wait after the `i-th` day to get a warmer temperature.

If there is no future day for which this is possible, put 0 instead.

📌 Example:
Input : T = [73, 74, 75, 71, 69, 72, 76, 73]  
Output: [1, 1, 4, 2, 1, 1, 0, 0]

==================================================================
🧠 My Initial Idea:

Naive way: For each day, loop forward to find next warmer day → O(n²)

✅ Optimization using Monotonic Stack:
- Maintain a **stack of indices** in **decreasing order of temperature**
- For each `i`, pop from stack while `T[i] > T[stack[-1]]`
  → means we found a warmer day for stack[-1]

- Then answer[stack[-1]] = i - stack[-1] (number of days waited)

🔁 Stack stores indices, not temperatures — so we can calculate distance!

==================================================================
🧮 Dry Run:

T = [73, 74, 75, 71, 69, 72, 76, 73]

i = 0, T[i] = 73 → stack = [0]  
i = 1, T[i] = 74 → 74 > 73 → pop 0, ans[0] = 1 → stack = [1]  
i = 2, T[i] = 75 → 75 > 74 → pop 1, ans[1] = 1 → stack = [2]  
i = 3, T[i] = 71 → 71 < 75 → stack = [2,3]  
i = 4, T[i] = 69 → 69 < 71 → stack = [2,3,4]  
i = 5, T[i] = 72 → 72 > 69 → pop 4, ans[4] = 1  
                     → 72 > 71 → pop 3, ans[3] = 2 → stack = [2,5]  
i = 6, T[i] = 76 → pop 5, ans[5] = 1 → pop 2, ans[2] = 4 → stack = [6]  
i = 7, T[i] = 73 → 73 < 76 → stack = [6,7]

Final Stack: [6,7] → No warmer days → ans[6] = 0, ans[7] = 0

==================================================================
🚧 Where I Went Wrong:

| Mistake                                   | Fix                                                   |
|-------------------------------------------|--------------------------------------------------------|
| ❌ Tried to compare all future days        | ✅ Used stack to keep indices of unresolved temperatures |
| ❌ Forgot to push current index to stack   | ✅ Always push `i` at end of loop                      |
| ❌ Calculated `T[i] - T[stack[-1]]`        | ✅ Correct: `i - stack[-1]` gives number of days       |

==================================================================
🛠️ Final Code (Python):

```python
def dailyTemperatures(T):
    res = [0] * len(T)
    stack = []  # store indices
    for i, temp in enumerate(T):
        while stack and T[i] > T[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res
