
````md
==================================================================
🧩 Problem: Subarray Sum Equals K
🔗 Link    : https://leetcode.com/problems/subarray-sum-equals-k/
📚 Topic   : Prefix Sum + Hashing
📈 Level   : Medium
==================================================================

📄 Description:
Given an integer array `nums` and an integer `k`, return the total number of **continuous subarrays** whose sum equals to `k`.

---

🧠 Initial Brute-force Thought:
I began with the most basic way of solving this by checking **all possible subarrays**.

```python
count = 0
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
        if curr_sum == k:
            count += 1
return count
```

### ✅ This worked fine for small inputs.

### ❌ But for large arrays, it gives **TLE (Time Limit Exceeded)** because it's **O(n²)**.

---

🔍 Where I Got Stuck:
I tried moving to prefix sum:

```python
psum = [0] * len(nums)
psum[0] = nums[0]
for i in range(1, len(nums)):
    psum[i] = psum[i - 1] + nums[i]
```

Then I tried:

```python
for i in range(len(nums)):
    if psum[i] >= k:
        count += 1
```

This didn’t work either 😕. I was just checking if prefix sums were greater than or equal to `k`, but not tracking **subarrays** correctly.

---

🧠 Key Insight:
Realized that we need to find:

```
current_prefix_sum - k = some_prefix_sum_we_have_seen
```

Which means:

* If `prefix_sum - k` is in hashmap, a valid subarray exists.
* Count how many times this sum has occurred.

---
dry run:
```
nums = [1, 2, 3],  k = 3
```
---

We use a **prefix sum** and a hash map (`prefix_sum_count`) to track how many times a given **prefix sum** has occurred.

At each step:

* We keep a `current_sum`
* We check if `current_sum - k` has appeared before — if yes, then a subarray summing to `k` ends here.
* We also store how many times each `current_sum` has appeared.

---

### 🧮 Let's walk through step by step:

Initialize:

* `count = 0`
* `prefix_sum = 0`
* `prefix_sum_count = {0: 1}`

---

#### 1. `num = 1`

* `prefix_sum = 0 + 1 = 1`
* `prefix_sum - k = 1 - 3 = -2` → not in map
* Update map: `{0:1, 1:1}`

---

#### 2. `num = 2`

* `prefix_sum = 1 + 2 = 3`
* `prefix_sum - k = 3 - 3 = 0` → in map! → add `prefix_sum_count[0] = 1` to count
* `count = 1`
* Update map: `{0:1, 1:1, 3:1}`

---

#### 3. `num = 3`

* `prefix_sum = 3 + 3 = 6`
* `prefix_sum - k = 6 - 3 = 3` → in map! → add `prefix_sum_count[3] = 1` to count
* `count = 2`
* Update map: `{0:1, 1:1, 3:1, 6:1}`

---

### 🧾 Final map: `{0:1, 1:1, 3:1, 6:1}`

---

### ✅ Final answer = `2` subarrays:

* `[1, 2]` → sum = 3
* `[3]` → sum = 3

---

✅ Final Optimized Code (Prefix Sum + HashMap):

```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}  # Important to handle exact match at index 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count
```

---

📌 Explanation:

* We use `prefix_map` to store the frequency of prefix sums seen so far.
* For each `prefix_sum`, we check if `prefix_sum - k` has been seen before.

  * If yes, it means there's a subarray ending at current index which sums to `k`.
* Increment count by frequency of that `prefix_sum - k`.

---

🛠️ Modifications That Helped Me Move Forward:

* Switched from double for-loops to prefix sum logic.
* Tried explicitly building prefix array but didn't link it to frequency.
* Finally understood that **hashmap frequency** is key to count all possible valid subarrays.

---

📊 Time Complexity:

* Brute-force: `O(n²)`
* Optimized: **O(n)**

🧠 Space Complexity:

* Brute-force: `O(1)`
* Optimized: **O(n)** for hashmap

---

💡 Core Observations:

* Hashmap allows us to **count subarrays in O(n)** time.
* Storing `{0:1}` handles subarrays starting from index `0`.
* Prefix Sum helps **track cumulative values** efficiently.
* We don't need to store actual subarrays — just the sums and their frequencies.

---

🔁 My Revisit Note:
This problem took \~5 hours across multiple iterations. Though I had seen it before, this time I actually understood the **why** behind every line. Understanding grew slowly through struggle — and it was worth it.

---

✅ Status: Solved with full understanding (Struggled → Fixed → Understood deeply)

```
