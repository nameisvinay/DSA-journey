
🧩 Problem: Subsets II
🔗 Link    : https://leetcode.com/problems/subsets-ii/
📚 Topic   : Recursion, Backtracking, Arrays
📈 Level   : Medium
==================================================================

📄 Description:
Given an integer array `nums` that may contain duplicates, return *all possible subsets (the power set)*.

**The solution set must not contain duplicate subsets.**

---

### ✅ Constraints:
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

---

### 🧠 Intuition:

This is a variation of the classic **Subsets** problem.  
But because `nums` contains **duplicates**, we must avoid creating **duplicate subsets**.

Instead of backtracking with visited sets, we use an **iterative subset construction** approach, and carefully track which subsets were added in the last iteration to avoid repetition.

---

### 🚀 Core Idea:

We generate subsets by **iteratively adding each number to existing subsets**, but:

    - If current number is a **duplicate**, we only combine it with the subsets created in the **previous step**
    - We track the start index of those new subsets using `start = len(res)`
    - For unique numbers, we combine with all subsets

---

## 🔄 Dry Run: 'nums = [1, 2, 2]'

### 📌 After Sorting:

        nums = [1, 2, 2]
        res = [[]]

---

    initally, result = [[]] --> start = 0   []

At iteration 1: 0th index :
                    nums[0] = 1  not duplicate(traverse from 0) => temp_start = 0
                    start = len(res) => 1
                                j -> (temp_start , len(res))            
                                    result.append([nums[i]] + result[j])

                result   =  [] + [1] --> [[],[1]]

At iteration 2: 1st index :
                    nums[1] = 2  not duplicate(traverse from 0) => temp_start = 0
                    start = len(res) => 2 
                                j -> (temp_start , len(res))
                                    result.append([nums[i]] + result[j])

                result   =  [[],[1]] + [2] --> []+[2], [1]+[2] --> [[],[1],[2],[1,2]]

At iteration 3: 2nd index :
                    nums[1] = 2  duplicate Found => 
                    temp_start = start (previous start as index point) 
                                j -> (temp_start , len(res))
                                    result.append([nums[i]] + result[j])
                    from traverse loop from index 2(start)

                result   =  [[],[1],[2],[1,2],[2,2],[1,2,2]

### ✅ Final Output:
      
                [[], [1], [2], [1,2], [2,2], [1,2,2]]


i always consfused here:
           - update start in next iteration. store start in temp_start if duplicate is found. and traverse loop from temp_start
           - if duplicate is not found, then traverse from 0
           - sorting is mandatory for find duplicates in adjacent.
                            



| Iteration | i | nums\[i] | Duplicate? | temp\_start | start (before append) | New Subsets Formed         | res after iteration                       |
| --------- | - | -------- | ---------- | ----------- | --------------------- | -------------------------- | ----------------------------------------- |
| 1         | 0 | 1        | ❌          | 0           | 1                     | '[] + [1]' → '[1]'         | '[ [], [1] ]'                             |
| 2         | 1 | 2        | ❌          | 0           | 2                     | '[] + [2]', '[1] + [2]'    | '[ [], [1], [2], [1,2] ]'                 |
| 3         | 2 | 2        | ✅          | 2           | 4                     | '[2] + [2]', '[1,2] + [2]' | '[ [], [1], [2], [1,2], [2,2], [1,2,2] ]' |
      

---

## ✅ Code (Python)

        def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = [[]]
            start = 0
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    temp_start = start
                else:
                    temp_start = 0
                
                start = len(res)
                for j in range(temp_start, len(res)):
                    res.append(res[j] + [nums[i]])
            
            return res

---

## 🧠 Time and Space Complexity

      * **Time:**  O(2^n) → Number of subsets in power set
      * **Space:** O(2^n) → Resultant subset list

---

## ✅ Key Takeaways

    * Sort the input to handle duplicates correctly
    * Use 'start = len(res)' to know which subsets were added in the previous round
    * When encountering a duplicate, only extend the subsets added in the last round
    * This technique is useful in similar problems like:

              - `Combination Sum II`
              - `Permutations II`
              -  Backtracking with duplicates

---

confused part: (revisit to remember)

    >  When a duplicate is found**, we store the **previous 'start' ** (which points to where new subsets started in the last round)
    >  into 'temp_start' **before** updating 'start' to the new length of the result.

---

### 🔁 Here’s the exact flow:

        
        if nums[i] == nums[i - 1]:         # 🟡 Duplicate found
            temp_start = start             # ✅ Save previous boundary
        else:
            temp_start = 0                 # 🚀 Use all subsets if unique
        
        start = len(result)                # 🆕 Mark new start boundary
        

* So `temp_start` = **where we begin forming new subsets**
* And `start` = **gets updated after we finish adding the new subsets**

---

### ✅ Let’s freeze this in a moment:

nums = [1, 2, 2]

    At 'i = 2' (duplicate 2):
    
    * Last time (when we added [2], [1,2]), we started from index 'start = 2'
    * So now:
  
          temp_start = start = 2
          start = len(result) = 4
  

Now we do:

    for j in range(temp_start, len(result)):  # j in range(2, 4)
        result.append(result[j] + [2])

So:
    * [2] + 2 → [2,2]
    * [1,2] + 2 → [1,2,2]

    ✅ Subsets formed from only the *new ones* from previous round.

---

### 📌 Final Recap:
        > 👉 **'temp_start' lets you “lock” the last starting point**
        > 👉 **'start' gets freshly updated each time**
        > 👉 This combo gives you control over what to use, and avoids duplicates 💯

