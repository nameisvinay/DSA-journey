
---

````md
==================================================================
🧩 Problem: Product of Array Except Self  
🔗 Link    : https://leetcode.com/problems/product-of-array-except-self/  
📚 Topic   : Arrays  
📈 Level   : Medium  
==================================================================

## 📝 Description:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

- You must solve it **without using division**
- In **O(n)** time complexity.
- Optimize space too if possible.

---

## ❌ Brute Force Approach (TLE)
For each index, loop over the array and calculate product of all elements **except the current index**.

### 🔍 Thought Process:
- For every `i`, do another loop and multiply everything except `i`
- Store result in an output array

### ⛔ Mistake:
- Time complexity is **O(n²)**
- Works for small input but will timeout

---

## 🔁 My First Optimized Attempt (with Prefix and Suffix arrays)
I tried using two arrays:
- `prefix[i]` stores product of all elements to the left
- `suffix[i]` stores product of all elements to the right

### ⚠️ Issue I Faced:
```py
for i in range(len(nums)-1, -1, -1):
    prod = 1
    for j in range(i+1, len(nums)):
        prod *= nums[j]
    suffix[i] = prod
````

I realized this loop runs in O(n²). So even though it *looked* optimal, it was still brute inside.

---

## ✅ Final Optimal Approach (O(n) Time, O(1) Extra Space)

### ✨ Idea:

* First pass: compute prefix product and store in answer\[]
* Second pass (from reverse): keep multiplying suffix and update answer\[i]

### 📌 Observation:

* I started loop from `1` (not `0`) for prefix since `answer[0]` stays `1`
* Similarly, suffix starts from `n-2` as last index is `1` by default

### ✅ My Final Code:

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # Prefix product pass
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            answer[i] = prod

        # Suffix product pass
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            answer[i] *= prod

        return answer
```

---

## 🔍 Dry Run:

For input: `nums = [1,2,3,4]`

* Prefix: `[1,1,2,6]`
* Suffix: `[24,12,4,1]`
* Final:  `[24,12,8,6]`

---

## 🧠 What I Learned:

* Prefix + Suffix pattern can avoid division
* Two-pass problems are common in arrays
* O(1) extra space means ignoring the output array
* Careful about loop boundaries, especially in reverse pass

---

## 🧩 Tags:

`Prefix-Product` `Two-Pass` `In-Place Array` `No Division` `O(n) Time` `Medium`

---
