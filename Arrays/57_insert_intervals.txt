---
# 🧩 Problem: Insert Interval
🔗 [Leetcode 57](https://leetcode.com/problems/insert-interval/)  
📚 Topic: Intervals, Arrays  
📈 Level: Medium  

---

## 📄 Description:
You are given an array of non-overlapping intervals sorted by their start times. Insert a new interval into the array and merge if necessary so that the result remains sorted and non-overlapping.

---

## ✅ Constraints:
- Intervals are sorted by start time.
- Merge any overlapping intervals after insertion.
- Optimize for O(n) time.

---

### my initial idea:

     - append newInterval when newInterval[0] < interval[i][0] . this check entire loop upto len(nums)-1.
     - if doesn't in between then directly add at end.

          found = False
          for i in range(len(intervals)):
              if newInterval[0] < intervals[i][0]:
                  intervals.insert(i,newInterval)
                  found = True
                  break
          
          if not found:
              intervals.append(newInterval)

    traverse over loop. and check if end > curr_start , means overlaps take maximum of both ends to end value.
    else append [start,end] to result.

          start,end = intervals[0]

        for i in range(1,len(intervals)):
            curr_start , curr_end = intervals[i]

            if end < curr_start:
                ans.append([start,end])
                start = curr_start
                end = curr_end
            else:
                end = max(end , curr_end)
        
        ans.append([start,end])
  -----
  
  final code based on my intuiton: 

        if not intervals:
            return [newInterval]
        
        found = False
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i,newInterval)
                found = True
                break
        
        if not found:
            intervals.append(newInterval)
        
        ans = []
        start,end = intervals[0]

        for i in range(1,len(intervals)):
            curr_start , curr_end = intervals[i]

            if end < curr_start:
                ans.append([start,end])
                start = curr_start
                end = curr_end
            else:
                end = max(end , curr_end)
        
        ans.append([start,end])

        return ans

    But here [insert(i,element)]  ---> takes n elemnts move right --> O(n) which affects time complexity. rather slow down the traversing.
    we cannot optimized this method as no other option to reduce time complexity of insert (only in linkedlist its possible for O(1). 
         
### from others approachs:  
      i got another approach instead of insertion we can do other approach merge updation.

      
## 💡 Intuition & Key Concepts:

      We split the problem into **3 parts**:
      
      ### 1. ➕ Add all intervals that end before `newInterval[0]`  
      These intervals do not overlap — append directly.
      
      ### 2. 🔁 Merge all overlapping intervals  
      While `intervals[i][0] <= newInterval[1]`, do:
      ```python
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      ````

### 3. ➕ Add all remaining intervals

    These come after the merged newInterval — append directly.

---

## 🔍 Dry Run Example

    **Input**:
    
    ```python
    intervals = [[1,3], [6,9]]
    newInterval = [2,5]
    ```
    
    **Process**:
    
    * `[1,3]` overlaps with `[2,5]` → merge to `[1,5]`
    * `[6,9]` comes after → append as is
    
    **Result**:
    
    ```python
    [[1,5], [6,9]]
    ```

---

## 🧠 Doubts Clarified

### ❓ Why use `min()` and `max()`?

To **merge overlapping intervals**, we continuously shrink and expand the range.

### ❓ Why avoid `.insert()`?

Python's `insert()` is O(n), not optimal. Instead, build the result using a result list `res`.

### ❓ What does this line do?

```python
while i < n and intervals[i][1] < newInterval[0]:
    res.append(intervals[i])
```

It collects all intervals **before** the new interval — no overlap.

### ❓ What if interval is greater than newInterval?

Then it's added **after** merging phase, since it no longer overlaps.

### ❓ What does merging do?

We **update** the `newInterval` to include all overlaps:

```python
newInterval[0] = min(...)
newInterval[1] = max(...)
```

---

## ✅ Final Optimized Code (O(n) Time)

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. Add intervals after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

---

## 🧮 Time & Space Complexity

* **Time:** O(n)
* **Space:** O(n)

---

## 🧷 Summary Points

* 🧠 Think in 3 phases: Before ⏩ Merge 🔁 After ⏩
* Avoid `.insert()` to keep O(n) time
* Merge using `min` and `max`
* Clear and readable code using 3 clean loops

---

```
