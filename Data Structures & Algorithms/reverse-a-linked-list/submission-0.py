# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous_node = None

        while head != None:      # node3 with next as None
            new_head = head.next # new_head = None
            head.next = previous_node # for node2, becomes node1
            previous_node = head # node2 becomes previous_node for node3
            head = new_head # head becomes node 3

        
        return previous_node
        