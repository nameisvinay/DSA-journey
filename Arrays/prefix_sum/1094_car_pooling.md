

`````md

==================================================================
🧩 Problem: 1094. Car Pooling  
🔗 Link   : https://leetcode.com/problems/car-pooling/  
📚 Topic  : Arrays / Prefix Sum / Greedy  
📈 Level  : Medium  
==================================================================

### 📄 Description:

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and
the locations to pick them up and drop them off are fromi and toi respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true


---

### ✅ Constraints:
    1 <= trips.length <= 1000
    trips[i].length == 3
    1 <= numPassengersi <= 100
    0 <= fromi < toi <= 1000
    1 <= capacity <= 105

`````
---

### inital idea: (bruteforce)
              
    trips = [[2,1,5],[3,3,7]], capacity = 4   

              num    from   to
               2      1      5
               3      3      7


                                 1    2   3   4   5   6   7
                  
                                 2    2   2   2                          at 5 passenger drop off
                                          3   3   3   3                  at 7 passenger drop off 
                                _____________________________
                                 2    2   5   5   5   3   3
                                          ↑
                                      here crossed capacity(4) so return False


                      ans = [0]*1001   ---> length we dont know so 1001 is limit (given in constraints)
                      for num,start,end in trips:
                          for i in range(start,end):
                              ans[i] += num
                              if ans[i] > capacity:
                                  return False
                      return True
       

### ✅ Approach: Difference Array + Prefix Sum

#### 🔑 Core Idea:
          Rather than updating every index between `from` and `to`, we apply a **difference array trick**:
              - Mark +`num_passengers` at the start
              - Mark -`num_passengers` at the end
              - Then do a **prefix sum** to track total passengers at each point

          when using prefix its very frequent and better to remember pattern.
                      ans[start] += num
                      ans[end] -= num

              ans = [0]*1001

              trips = [[2,1,5],[3,3,7]], capacity = 4   

              num    from   to
               2      1      5
               3      3      7

                                 1  2  3  4  5  6  7
                                 2  0  0  0  -2
                                       3  0  0  0 -3
                                _____________________
                                2  0   3  0  -2   -3   ---> prefix sum of ans if found > capacity return False
                                
                    prefix_sum  2  2   5  5   3    0
                                       ↑
                                       > capacity(4)


When prefix sum is applied, it fills the actual number of passengers in the car at each location.

---

### 🧠 Why Subtract at `end`?

The interval is treated as **[from, to)**:
    - Passengers are **in the car** at locations: `from, from+1, ..., to-1`
    - They **drop off** at location `to`

That’s why we:
        ans[from] += num
        ans[to] -= num  

---

#### 🔁 Prefix Sum:

      ```python
      curr = 0
      for p in ans:
          curr += p
          if curr > capacity:
              return False
      ```

### ✅ Code (Python):

      ```python
      def carPooling(trips, capacity):
          ans = [0] * 1001  # Locations range from 0 to 1000
      
          for num, start, end in trips:
              ans[start] += num
              ans[end] -= num  # drop off at 'end'
      
          curr = 0
          for passengers in ans:
              curr += passengers
              if curr > capacity:
                  return False
          return True
      ```

---

### 🔁 Time & Space Complexity:

* **Time:** O(n + 1001) → Linear
* **Space:** O(1001) → Constant since location is bounded

---

### 🧠 Takeaway:

> This is a perfect example of using the **prefix sum + difference array trick** to optimize interval additions.
> Instead of simulating the entire timeline for every trip, we just log entry/exit points and simulate once.

---

### 💡 When to Use This Trick:

* Car Pooling / flight Booking systems
* Range updates
* Population changes over time
* Any “enter at `start`, leave at `end`” problems

---
