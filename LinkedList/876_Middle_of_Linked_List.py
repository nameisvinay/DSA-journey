# LeetCode 876. Middle of the Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/middle-of-the-linked-list/

"""
🧠 Problem:
Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second one.

Examples:
Input: [1,2,3,4,5]
Output: Node with value 3

Input: [1,2,3,4,5,6]
Output: Node with value 4
"""

# ✅ Approach 1: Count Nodes and Return Middle
# Time: O(N), Space: O(1)

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    temp = head
    count = 0
    while head:
        head = head.next
        count += 1 #counting starts after 1st head

    val = count//2 # This gives 0-based index directly

    if count == val == 1:
        return head

    new_count = 0
    while temp:
        if new_count == val: #checks with before count then we reach node matchs val.
            return temp
        new_count += 1
        temp = temp.next
    # if we check condition first,then it checks before new_count and gives from current temp
    # when 
    # considers new_count before current temp.


#better than previous approach
def middleNode(head):
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next

    mid = count // 2
    temp = head
    # for _ in range(mid):
    #     temp = temp.next
    while mid:
        temp = temp.next
        mid -= 1
    return temp


# ✅ Approach 2: Two Pointer (Fast and Slow)
# Time: O(N), Space: O(1)

def middleNode_2pointer(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

"""
📝 Notes:
- Both methods return the correct middle node.
- Approach 2 is cleaner and avoids a second loop.
- When length is even, returns the 2nd middle node (as required).
"""

