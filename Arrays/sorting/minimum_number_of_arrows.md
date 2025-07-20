
````markdown
==================================================================
🧩 Problem : Minimum Number of Arrows to Burst Balloons
🔗 Link    : https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
📚 Topic   : Array , Greedy, Sorting
📈 Level   : Medium
==================================================================

📄 Description:
 Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
 A balloon with xstart and xend is burst by an arrow shot at x if x_start <= x <= x_end. There is no limit to the number of arrows that can be shot.
 A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

  Input: points = [[10,16],[2,8],[1,6],[7,12]]
  Output: 2
  Explanation: The balloons can be burst by 2 arrows:
  - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
  - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].


My initial idea: 

1. choose a number and check if it satisfies the condition "x_start <= x <= x_end" for each point.
2. if done with all points. count number of arrows can hit . then increment number and again check.
3. for every iteration, increment arrow count if any arrow can hit the ballon.


Also another idea is:

- merging intervals, at first i though of merging intervals by sorted and where previous end <= curr_start. and take [min(start,curr_start) , max(end,curr_end)]
though this was correct optimal approach but realized all are merging into one single interval. so this dont work.

- then took help from chatgpt and mentioned my ideas.
    1. it says instead of taking max(end,curr_end] pick min(end,curr_end) to tighten intervals.
    2. then i did [min(start,curr_start) , min(end,curr_end)] --> so reached intervals that dont merge and tighten overlapping.


suprising my two idea works one for bruteforce and other is optimal greedy.


###bruteforce 
```python
        points.sort(key = lambda x:x[1])
        arrow = 0
        visited = [False]*len(points)

        while not all(visited):
            i = 0
            while i < len(points) and visited[i]:
                i += 1
            
            if i == len(points):
                break

            # ✅ Choose right end, not left start
            x = points[i][1]
            for j in range(len(points)):
                if not visited[j] and points[j][0] <= x <= points[j][1]:
                    visited[j] = True
                    
            arrow += 1
        return arrow

flow after coding:
  1. loop over condition of checking till all points to visit.
  2. initalize with i = 0. for picking number within in points[x,y] range.
  3. now check for either it was not yet visited and number you choose is within range. mark it as visited.
  4. till 'i' reach to end(length of points).after every new iteration increment arrow count.


---

###Optimal approach(Greedy)

```python
        points.sort()
        merge = [] #no need of this, i just included for better understandind in future
        start , end = points[0]
        arrow = 1

        for i in range(1,len(points)):
            curr_start,curr_end = points[i]

            if end >= curr_start:
                start = min(start,curr_start)
                end = min(end,curr_end)
            else:
                arrow += 1
                end = max(end,curr_end)
            
            merge.append([start,end])

        return arrow

#optimal --> tc -> O(nlogn) and sc -> o(1)  or O(n)-(if used new space)
