"""
##
🧩 Problem: Reorder List
🔗 Link    : https://leetcode.com/problems/reorder-list/
📚 Topic   : Linked List
📈 Level   : Medium
==================================================================

📄 Description:
Reorder the given singly linked list in-place such that:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You must not modify the values in the nodes, only node connections.

📌 Example:
Input  : [1, 2, 3, 4, 5]
Output : [1, 5, 2, 4, 3]

==================================================================
🧠 My inital Idea:

    1st half : 1 -> 2 -> 3
    2nd half : 4 -> 5 now reverse 2nd half 5 -> 4

    1 -> 2 -> 3 
    5 -> 4 -> None

just like connecting two linkedlist. [1 -> 5 -> 2 -> 4 -> 3 -> None]


------> before solving this have idea on problems : 
                  https://leetcode.com/problems/middle-of-the-linked-list/   --> to find mid
                  https://leetcode.com/problems/reverse-linked-list/         --> to reverse list


STEPS : 

step1 : Find mid and separate two halfs.

        disconnect at mid. for that find length and take length//2

            length = 0
            while head:
                head = head.next
                length += 1

            mid = length//2

        ❌ mistake Here: i moved head upto length which means head is None now. so always store orginal head in other variables.('ptr' as of now)
    
        ✅ Fix --->    
                    ```python
                    length = 0
                    ptr = head
                    while ptr:
                       ptr = ptr.next
                       length += 1
    
                 Find mid now:    mid = length//2
            

    --> To split first and second halfs:
                
            temp = curr = head  # always store head in temporaray variables.
            prev = None
            for _ in range(mid):  # Assume we got mid=2  move loop upto mid+1 (to reach upto Node 3)
               prev = temp     #always stays before mid
               temp = temp.next
               

                                        prev  mid
                                          ↓    ↓          
                             list :  1 -> 2 -> 3 -> 4 -> 5 -> None
                             index:  0    1    2    3    4


          * store temp in prev (before mid node. mid is first node of second half)
          * prev is last node of first half.

      ❌    I originally thought breaking first half isn’t needed, but it will create cycle during merge and pointer bugs when merging.

        But we need to disconnect at prev. this way after loop ends (loop going to mid+1)
        
            --> prev.next = None. (remember to initialize prev = None before loop starts to avoid errors)

                First Half:
                        list:  1 -> 2 -> None      
                        index: 0    1        
                    
                    At '2'(prev) first half ends and At '3'(mid position) second half start.
                    
                Second Half:
                        list: 3 -> 4 -> 5 -> None

        In both odd and even length lists, we treat mid as the boundary where we split the list into:
                        First Half → Nodes before mid
                        Second Half → Starts at mid

       
        mid = length//2 --> gives result when even length and/or with odd length. needs of (mid+1) which may critical to think later.

      ****   so avoid this for better cleaner code.

         
          use slow/fast pointer ---> gives middle exactly for both even and odd.
    
              ```python
              slow = fast = head
              prev = None
              while fast and fast.next:
                 prev = slow  
                 slow = slow.next
                 fast = fast.next.next
              prev.next = None   
              
                    prev  slow
                     |    |  
                1 -> 2 -> 3 -> 4 -> 5 -> None
                
                
              # Now `slow` is at start of 2nd half
              # `prev` is at end of 1st half
             
              slow is at mid position even / odd exactly (no need of mid+1 explicity) 
              temp = slow   #store slow in temp
          

        ❌ mistake : If your input linked list has less than 2 nodes (especially only 1 node), the while fast and fast.next loop.
                  will not run even once, so prev stays None. Then trying prev.next causes the error.
        
        ✅ Fix :  Add a guard condition before prev.next = None

                        ```python
                        if prev:
                            prev.next = None   # only disconnect if prev exists
                        ```   
            means initially prev is at None. 
            so to make prev to move forward we need atleast >2 nodes in list.else slow and fast pointer doesnot move.prev still at None(which raises error)
        
            more better way to for early return.
            add at beginning of code.

            ### 🛡️ Edge Case Handling

                    If list has 0 or 1 nodes, no need to reorder.
                    
                    ```python
                    if not head or not head.next:
                        return
                    ```


 step2: Reverse 2nd half
   
           ```python
           rev_temp = None
           while slow:
               next_node = slow.next
               slow.next = rev_temp
               rev_temp = slow
               slow = next_node

        second half : 5 -> 4 -> 3 -> None
            
            
      
step3:  merging two halfs

                                                                  first
               ```python                                            ↓ 
               first = head                                         1 -> 2 -> None
               second = rev_temp                                    5 -> 4 -> 3 -> None
               while first:                                         ↑
                   tmp1 = first.next                              second
                   tmp2 = second.next
    
                   first.next = second
                   second.next = tmp1                                 tmp1
                                                                        ↓ 
                   first = tmp1                              1 -> 2 -> None
                   second = tmp2                             5 -> 4 -> 3 -> None
                                                                  ↑
                                                                tmp2
    
        ❌ Mistake: here i got stuck because i only check condition for when second ends. but what if first reachs to none before second reach.
            it raised error.
        
        ✅ Fix:  while first and second


        ❌ Mistake: Another error i got stuck:
        
            after first(1st half node) connected to second(2nd half node). and second of 2nd half node to next node of 1st half it has None. 
            which raised error.
                
        ✅fix ---->
    
            only connected to first half node when it exists else connected to same second half node
    
                ```python
                first.next = second
                   if tmp1 is None:
                       second.next = tmp2
                   else:
                       second.next = tmp1 
 

   ------> code worked <-----

===============================================================================

🚧 Where I Went Wrong:

    | Mistake                                                | Fix                                             |
    | ------------------------------------------------------ | ----------------------------------------------- |
    | ❌ Used `length // 2` to find mid (buggy in edge cases) | ✅ Used slow/fast pointer                        |
    | ❌ Didn't disconnect first half → caused cycles         | ✅ `prev.next = None` to break                   |
    | ❌ Merge logic broke for odd-length list                | ✅ Check both `first` and `second` while merging |
    | ❌ Forgot edge case: 0 or 1 node                        | ✅ Early return guard clause                     |
    | ❌ Assumed both lists are same length                   | ✅ Careful handling inside `while` merge loop    |

===============================================================================
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find middle using slow-fast
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None  # break list into two parts

    # Step 2: Reverse second half
    rev_temp = None
    while slow:
        next_node = slow.next
        slow.next = rev_temp
        rev_temp = slow
        slow = next_node

    # Step 3: Merge two halves
    first = head
    second = rev_temp
    while first and second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        if tmp1 is None:
            second.next = tmp2
        else:
            second.next = tmp1

        first = tmp1
        second = tmp2


"""
==================================================================
🧪 Test Case:
Input : [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

📝 Notes:
- Pointer manipulation heavy — draw on paper helps.
- Variants:
  - Palindrome Linked List
  - Rearranging List in Zig-Zag
==================================================================
"""
