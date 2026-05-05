# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodes = set()

        while head is not None:
            if head not in nodes:
                nodes.add(head)
            else:
                return True
            head = head.next
        
        return False
        