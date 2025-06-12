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
            
    --> loop head upto mid and at last in mid position connect to None.

            temp = curr = head
            for _ in range(mid):  # we got mid=2
               temp = temp.next
            
         list :  1 -> 2 
         index:  0    1 

            but we need to disconnect at 2nd position that means mid+1.so loop till mid+1(3)

            
            list:  1 -> 2 -> 3       
            index: 0    1    2     #loop till mid+1 so reaches to 3 where our first half needs to be end.

            At '2' first start loop ends and At '3' second half start.
            

mistake 2: moves to mid times(start of 2nd half) but doesn't break the list.it will create cycle during merge.

Fix ---->
            when temp reached mid+1 times then at last position connect to None.

                 |
            1 -> 2 -> None    #disconects first half.
            0    1   

            temp = curr = head
            for _ in range(mid+1):
               prev = temp   #store temp to prev until mid, first half stops at before mid
               temp = temp.next
            prev.next = None  #when reached before to mid position then connect to None

            First half : 1 -> 2 -> None

        In both odd and even length lists, we treat mid as the boundary where we split the list into:
                        First Half → Nodes before mid
                        Second Half → Starts at mid
            

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
           while second:                                        ↑
               tmp1 = first.next                              second
               tmp2 = second.next

               first.next = second
               second.next = tmp1                            tmp1
                                                              ↓ 
               first = tmp1                              1 -> 2 -> 3 -> None
               second = tmp2                             5 -> 4 -> None
                                                              ↑
                                                            tmp2



   ------> code worked <-----

      instead of making code optimized and better.
      
         length//2 --> gives different result when even length and/or with odd length.
         To manage it we need dummy to attach before linkedlist. so it starts with 0-indexed.
         so avoid this for better cleaner code.

         
      use slow/fast pointer ---> gives middle exactly for both even and odd.

      slow = fast = head
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
     
      slow is at mid position even / odd exactly
      temp = slow   #store slow in temp

      ---> this helps me to get to mid position.

==================================================================
🚧 Where I Went Wrong:

❌ Mistake 1: Used `length//2` and looped up to mid — worked for some cases, failed in others.  
✅ Fix 1   : Used slow/fast pointer approach to accurately find mid for both odd/even lists.

❌ Mistake 2: Didn't disconnect the first half from the second → led to cycles while merging.  
✅ Fix 2   : Used `prev.next = None` to properly break the list at mid.

❌ Mistake 3: Merge logic incorrect for odd-length list.  
✅ Fix 3   : Carefully merged nodes and broke when necessary to avoid dangling pointers.

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
    slow, fast = head, head
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
