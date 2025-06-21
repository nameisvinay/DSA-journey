## 🔁 DSA Revision Tracker

Tracking my revision progress across multiple DSA topics from Arrays to LinkedList.

---

### ✅ Completed

   - 📁 Arrays
   - 📁 Prefix Sum
   - 📁 Linkedlist
   - 📁 Queues
   - 📁 Stacks
   - 📁 Binar Search

### 🔁 Revisit Needed

* [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) – Hard
* [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) – Hard
* [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) – Medium
* [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) – Easy
* [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) – Medium
* [456. 132 Pattern](https://leetcode.com/problems/132-pattern/) – Medium
* [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) – Hard
* [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) – Hard
* [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) – Easy
* [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) – Medium
* [57. Insert Interval](https://leetcode.com/problems/insert-interval/) – Medium
* [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) – Medium
* [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) – Medium
* [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) – Medium
* [Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array/) – Medium
* [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) – Medium
* [457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/description/) - Medium
* [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) – Medium
* [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) – Hard
* [Count Inversions](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1) - Medium
* [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) – Medium
* [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) – Medium
* [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) - Medium

### ❌ Full Rework

* [57. Insert Interval](https://leetcode.com/problems/insert-interval/) – Medium
* [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) – Medium
* [90. Subsets II](https://leetcode.com/problems/subsets-ii/) – Medium
* [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) – Hard
* [Count Inversions](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1) - Medium
* [2064. Minimized Maximum of Products Distributed to Any Store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) - Medium

---

### 📁 Arrays

* [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/) – Easy
  - start with 0. check when prev != curr. if found   (careful about condition check) if i==len or nums[i-1]+1 == nums[i] 
  - check length from start if more than 1. i-start > 1
  - then str(nums[start])+ '->'+ str(nums[end])  or f"{start} -> {end}"
  - else start
* [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) – Easy
   - count till found 1. if not take maximum of count and reset count to new check
* [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) – Easy
    - atleast one unique which mean k starts from 1.
* [268. Missing Number](https://leetcode.com/problems/missing-number/) – Easy
    - sum of n natural number
    - another approach (xor for all 0 to n+1 and xor of each num in nums) xor of both is our result
* [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) – Easy
    - place pointer at 0 and traverse till found != 0 in array if found swap with pointer and increment pointer.
* [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) – Easy
    - initailize max_length = 1
    - traverse from 1 to len(nums) and through increasing sequence.
    - if found decreased num , take max_length = r-l+1
    - traverse all over nums and return max_length
* [717. 1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) – Easy
    - 0 -> 1bit | 1 -> 2bit
    - initialize i = 0
    - if i == 1 increment 2 because its 2bit. else 1
    - if i reached to len(nums)-1 its 1 bit. if goes out of index its 2bit
* [57. Insert Interval](https://leetcode.com/problems/insert-interval/) – Medium
* [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) – Medium
* [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) – Medium
  
### 📁 Two Pointers

* [344. Reverse String](https://leetcode.com/problems/reverse-string/) – Easy
* [27. Remove Element](https://leetcode.com/problems/remove-element/) – Easy
* [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) – Medium
* [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) – Medium
* [15. 3Sum](https://leetcode.com/problems/3sum/) – Medium
* [18. 4Sum](https://leetcode.com/problems/4sum/) – Medium
* [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) – Medium
* [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) – Medium
* [457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/description/) - Medium

### 📁 Strings

* [14.Longest Common prefix](https://leetcode.com/problems/longest-common-prefix/description/) - Easy


### 📁 Sliding Window

* [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) – Medium
* [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) – Medium
* [3364. Minimum Positive Sum Subarray](https://leetcode.com/problems/minimum-positive-sum-subarray/) – Medium
* [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) – Medium
* [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) – Medium
* [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) – Medium
* [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) – Medium
* [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) – Medium
* [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) – Medium
* [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) – Medium
* [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) – Hard

### 📁 Prefix Sum

* [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) – Easy
     - loop from 1 to n
     - prefix[i] += prefix[i-1] --> will update prefixs inplace
* [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) – Easy
     - check when left sum and right equal.then return pivot.
     - rsum = total - nums[i] - left_sum
     - if left_sum == right_sum return pivot
* [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) – Easy
* [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) – Easy
* [1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) – Easy
* [1991. Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) – Easy
* [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) – Medium
* [Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array/) – Medium

### 📁 Binary Search

* [704. Binary Search](https://leetcode.com/problems/binary-search/) – Easy
* [278. First Bad Version](https://leetcode.com/problems/first-bad-version/) – Easy
* [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) – Medium
* [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) – Easy
* [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) – Medium
* [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) – Medium
* [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) - Medium
* [2064. Minimized Maximum of Products Distributed to Any Store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) - Medium

### 📁 Bit Manipulation

* [136. Single Number](https://leetcode.com/problems/single-number/) – Easy
* [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) – Easy
* [231. Power of Two](https://leetcode.com/problems/power-of-two/) – Easy
* [137. Single Number II](https://leetcode.com/problems/single-number-ii/) – Medium
* [260. Single Number III](https://leetcode.com/problems/single-number-iii/) – Medium
* [338. Counting Bits](https://leetcode.com/problems/counting-bits/) – Easy
* [477. Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/) – Medium
* [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) – Medium
* [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) – Easy
* [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) – Medium
* [461. Hamming Distance](https://leetcode.com/problems/hamming-distance/) – Easy
* [476. Number Complement](https://leetcode.com/problems/number-complement/) – Easy
* [1009. Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) – Easy
* [2643. Row With Maximum Ones](https://leetcode.com/problems/range-product-queries-of-powers/) – Medium
* [1356. Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) – Easy

### 📁 Hashing

* [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) – Easy
* [1. Two Sum](https://leetcode.com/problems/two-sum/) – Easy
* [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) – Easy
* [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) – Easy
* [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) – Easy
* [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) – Medium
* [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) – Medium
* [2414. Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) – Medium
* [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) – Medium
* [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) – Medium
* [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) – Medium
*  [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) – Hard

### 📁 Recursion

* [78. Subsets](https://leetcode.com/problems/subsets/) – Medium
* [90. Subsets II](https://leetcode.com/problems/subsets-ii/) – Medium
* [231. Power of Two](https://leetcode.com/problems/power-of-two/) – Easy
* [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) – Easy
* [326. Power of Three](https://leetcode.com/problems/power-of-three/) – Easy
* [342. Power of Four](https://leetcode.com/problems/power-of-four/) – Easy
* [2094. Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers/) – Easy

### 📁 Sorting

* [75. Sort Colors](https://leetcode.com/problems/sort-colors/) – Medium
* [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) – Medium
* [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) – Easy
* [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) – Hard
* [2164. Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) – Easy
* [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) – Medium
* [Kth Smallest](https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1) - Medium
* [Count Inversions](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1) - Medium

### 📁 Stacks

* [155. Min Stack](https://leetcode.com/problems/min-stack/) – Medium
* [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) – Easy
* [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) – Easy
* [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) – Medium
* [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) – Medium
* [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) – Medium
* [456. 132 Pattern](https://leetcode.com/problems/132-pattern/) – Medium
* [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) – Hard
* [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) – Hard

### 📁 Queues

* [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) – Easy
* [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) – Easy
* [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) – Easy
* [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) – Hard
* [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) – Medium
* [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) – Medium

### 📁 Linkedlist

* [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) – Easy  
* [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) – Easy  
* [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) – Medium  
* [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) – Medium  
* [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) – Hard  
* [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) – Medium  
* [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) – Medium  
* [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) – Easy  
* [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) – Easy
  
---

📝 **Updated on:** 2025-06-21
