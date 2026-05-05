# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        nodes_list = []

        node = head

        while node is not None:
            nodes_list.append(node)
            node = node.next
        
        if len(nodes_list) == 1:
            return

        while len(nodes_list) > 0:

            first_node = nodes_list.pop(0)
            last_node = nodes_list.pop()

            second_node = first_node.next
            first_node.next = last_node
            if len(nodes_list) > 0:
                last_node.next = second_node
            else:
                last_node.next = None
            if len(nodes_list) == 1:
                last_node = nodes_list.pop()
                last_node.next = None


        