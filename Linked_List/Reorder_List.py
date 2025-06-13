"""
==================================================================
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


    --> I originally thought breaking first half isn’t needed, but it actually prevents cycles and pointer bugs when merging.
    
    --> Even though the reversed list ends in None, the first half still points into the old second half unless you break it.

    So yes — you must break first half manually using prev.next = None
    It’s not for the second half — it's for cutting the old connection from first half to second half.



Now separate list into two halves.

       --> disconnect at mid. for that find length and take length//2

            length = 0
            while head:
               head = head.next
               length += 1

mistake 1: moved head upto length which means head is None now. so always store orginal head in other variables.('ptr' as of now)

Fix --->
            length = 0
            ptr = head
            while ptr:
               ptr = ptr.next
               length += 1

         Find mid now:    mid = length//2
            
    --> loop head upto mid and at last in before mid position connect to None.

            temp = curr = head
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

    *--> I originally thought breaking first half isn’t needed, but it will create cycle during merge and pointer bugs when merging.

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
          

mistake : If your input linked list has less than 2 nodes (especially only 1 node), the while fast and fast.next loop.
          will not run even once, so prev stays None. Then trying prev.next causes the error.

Fix :  Add a guard condition before prev.next = None
                if prev:
                    prev.next = None   # only disconnect if prev exists
                    
    means initially prev is at None. 
    so to make prev to move forward we need atleast >2 nodes in list.else slow and fast pointer doesnot move.prev still at None(which raises error)

    more better way to for early return.
    add at beginning of code.
    
            if not head or not head.next:
                return


   ---> Reverse 2nd half

           rev_temp = None
           while temp:
               next_node = temp.next
               temp.next = rev_temp
               rev_temp = temp
               temp = next_node

        second half : 5 -> 4 -> 3 -> None
            
            
      
   ---> now merge two halfs.                                   first
                                                                ↓ 
           first = curr                                         1 -> 2 -> None
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

        here i got stuck because i only check condition for when second ends. but what if first reachs to none before second reach.
        it raised error.
        
    Fix:  while first and second

    Another error i got stuck:
    
        after first(1st half node) connected to second(2nd half node). and second of 2nd half node to next node of 1st half it has None. 
        which raised error.
            
    fix ---->

        only connected to first half node when it exists else connected to same second half node
         
            first.next = second
               if tmp1 is None:
                   second.next = tmp2
               else:
                   second.next = tmp1 
 

   ------> code worked <-----

==================================================================
🚧 Where I Went Wrong:

❌ Mistake 1: Used `length//2` and looped up to mid — worked for some cases, failed in others.  
✅ Fix 1   : Used slow/fast pointer approach to accurately find mid for both odd/even lists.

❌ Mistake 2: Didn't disconnect the first half from the second → led to cycles while merging.  
✅ Fix 2   : Used `prev.next = None` to properly break the list at mid.

❌ Mistake 3: Merge logic incorrect for odd-length list.  
✅ Fix 3   : Carefully merged nodes and broke when necessary to avoid dangling pointers.

❌ Mistake 4: checked condition only for second half to finish
✅ Fix 4   : need loop to check both halfs.

❌ Mistake 5: after first(1st half node) connected to second(2nd half node). and second of 2nd half node to next node of 1st half it has None. 
              which raised error.
✅ Fix 5   :  only connected to first half node when it exists else connected to same second half node
==================================================================
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
    slow, fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None  # break list into two parts

    # When loop ends, slow is at middle (i.e., start of second half).
    # prev is the last node of first half → we do prev.next = None to split the list.

    # Step 2: Reverse second half
    #reverse temp
      rev_temp = None
      while temp:
            next_node = temp.next
            temp.next = rev_temp
            rev_temp = temp
            temp = next_node


        first = curr
        second = rev_temp
        while second:  
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            if tmp1 is None:
                second.next = tmp1
            else:
                second.next = tmp2

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
