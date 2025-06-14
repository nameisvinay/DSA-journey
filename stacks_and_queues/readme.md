# 📦 Stacks & Queues – Problem Tracker

Tracking my understanding, mistakes, and final solutions.

---

## ✅ Completed

### 496. Next Greater Element I
📌 Status: Confident  
💡 Notes: Classic use of **monotonic stack**. First real warm-up into "Next Greater" logic.

### 503. Next Greater Element II
📌 Status: Confident  
💡 Notes: Same as previous but **circular array** handling via modulo. Understood the trick clearly.

### 225. Implement Stack using Queues
📌 Status: Confident  
💡 Notes: Queue + 2 approaches (costly push vs costly pop). Did single queue trick using rotate.

### 232. Implement Queue using Stacks
📌 Status: Confident  
💡 Notes: Two stacks (input + output). Dry-run made it easier to understand flow of lazy transfers.

### 933. Number of Recent Calls
📌 Status: Confident  
💡 Notes: Simple use of queue. Good warm-up before hitting medium-level queue problems.

---

## 🔁 Needs Revisit

### 735. Asteroid Collision
📌 Status: Revisit  
💡 Notes: Made mistake with **signs and order of collisions**. Stack was clear but logic messy.

### 215. Kth Largest Element in an Array
📌 Status: Revisit  
💡 Notes: Used sorting but forgot how to apply **min-heap efficiently**. Need to review `heapq`.

### 901. Online Stock Span
📌 Status: Revisit  
💡 Notes: Missed how to store both **price and span** in stack. Requires dry-run to fully lock logic.

### 622. Design Circular Queue
📌 Status: Revisit  
💡 Notes: Logic was okay but struggled with **modulo wrap-around** and head/tail edge cases.

### 90. Subsets II
📌 Status: Revisit  
💡 Notes: Confused when to skip duplicates in recursion. Understand backtracking + sorting.

---

## ❌ Need Full Rework

### 84. Largest Rectangle in Histogram
📌 Status: Forgot  
💡 Notes: Didn't understand **monotonic stack** fully. Stuck on index boundaries and area calc. Revisit full approach with dry-run.

### 239. Sliding Window Maximum
📌 Status: Forgot  
💡 Notes: Struggled with deque logic. Couldn't implement efficient removal logic within the window size.

---

## 🧠 Key Concepts Reviewed

- Monotonic Stack (for NGE / Histogram / Sliding Window)  
- Stack simulation using Queues (and vice versa)  
- Deques for fixed-size window problems  
- Backtracking in subsets with duplicate handling  
- Heap for Kth Largest (min-heap logic)  
- Circular queue design (wrap-around, size tracking)

---

📝 *Updated on: 2025-06-14*
