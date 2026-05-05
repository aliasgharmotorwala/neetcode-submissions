# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        start_node = None
        previous_node = None

        # continue until both lists ends
        while list1 is not None or list2 is not None: #2 3

            if list1 is None or (isinstance(list1, ListNode) and isinstance(list2, ListNode) and list1.val > list2.val):
                node = ListNode(val=list2.val)
                next_node = node
                list2 = list2.next
            elif list2 is None or (isinstance(list2, ListNode) and isinstance(list2, ListNode) and list1.val < list2.val): 
                node = ListNode(val=list1.val)
                next_node = node
                list1 = list1.next
            else:
                node = ListNode(val=list1.val)
                temp_node = ListNode(val=list2.val)
                node.next = temp_node
                next_node = temp_node
                list1 = list1.next
                list2 = list2.next

            if previous_node:
                previous_node.next = node
            else:
                start_node = node
            previous_node = next_node

        return start_node
            


