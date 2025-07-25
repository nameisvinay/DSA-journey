````md
==================================================================
🧩 Problem: Range Sum Query - Immutable  
🔗 Link    : https://leetcode.com/problems/range-sum-query-immutable/  
📚 Topic   : Prefix Sum  
📈 Level   : Easy  
==================================================================

### 📄 Description:
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

    Example 1:
    
    Input
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
    [null, 1, -1, -3]
    
    Explanation
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.

````
---

### 🧠 Approach: Prefix Sum

#### 🔸 Prefix Sum Concept:
          To avoid repeated summation, we precompute the cumulative sum in a 'prefix[]' array.

```
- prefix[i] = sum(nums[0] ... nums[i])
- Then:  
      - If 'left > 0': 
              "sumRange(left, right) = prefix[right] - prefix[left - 1]" 
      - If 'left == 0':
              "sumRange = prefix[right]"   --->  ❌ Crashes for 'left = 0' (accesses "prefix[-1]")

```
---

### ✅ Final Code (0-based Prefix + Edge Case Check)  --- 0-indexed 

      ```python
      class NumArray:
          def __init__(self, nums: List[int]):
              self.prefix = [0] * len(nums)
              self.prefix[0] = nums[0]
              for i in range(1, len(nums)):
                  self.prefix[i] = self.prefix[i - 1] + nums[i]
      
          def sumRange(self, left: int, right: int) -> int:
              if left == 0:
                  return self.prefix[right]
              return self.prefix[right] - self.prefix[left - 1]
      ````

---

### ✅ Alternate Version (1-based Prefix Array – Cleaner)

        ```python
        class NumArray:
            def __init__(self, nums: List[int]):
                self.prefix = [0] * (len(nums) + 1)
                for i in range(len(nums)):
                    self.prefix[i + 1] = self.prefix[i] + nums[i]
        
            def sumRange(self, left: int, right: int) -> int:
                return self.prefix[right + 1] - self.prefix[left]
        ```

---

### 🔍 Dry Run Example

```
nums = [3, 7, 2, 5]

#### Prefix Array (1-based):

          Index :   0   1   2   3   4
          Prefix:   0   3  10  12  17


* sumRange(1, 2) = prefix[2+1] - prefix[1] = 12 - 3 = 9 ✅
* sumRange(0, 3) = prefix[3+1] - prefix[0] = 17 - 0 = 17 ✅

```
---

### ⚠️ Mistakes to Avoid

| Mistake                               | Why it fails                                     |
| ------------------------------------- | ------------------------------------------------ |
| prefix[right] - prefix[left - 1]      | ❌ Crashes for 'left = 0' (accesses "prefix[-1]") |
| Recomputing sum in every query        | ❌ Leads to TLE for large input                   |
| Not allocating prefix of size 'n + 1' | ❌ Causes index errors in 1-based version         |

---

###  Time & Space Complexity

| Method      | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Constructor | O(n)            | O(n)             |
| sumRange()  | O(1)            | —                |

---

### 🧠 Summary:

* Precomputing prefix sums gives **constant time** query lookup.
* Safer and cleaner to use **1-based prefix array** to avoid edge cases.
* A classic example of trading **extra space for faster queries**.

-----
