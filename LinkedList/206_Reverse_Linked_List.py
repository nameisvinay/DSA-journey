# LeetCode 206. Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/

"""
🧠 Problem:
Reverse a singly linked list.

Example:
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# ✅ Final Working Code
# Time: O(N), Space: O(1)

def reverseList(head):
    prev = None
    while head:
        next_node = head.next     # save next
        head.next = prev          # reverse pointer
        prev = head               # move prev forward
        head = next_node          # move head forward
    return prev

"""
📝 Notes:
- Standard in-place reversal using 3 pointers.
- Important: store head.next before modifying.
"""

