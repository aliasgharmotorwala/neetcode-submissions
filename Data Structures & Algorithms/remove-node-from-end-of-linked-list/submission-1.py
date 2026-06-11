# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        nodes_list = []

        node = head

        while node is not None:
            nodes_list.append(node)
            node = node.next

        node_to_remove = len(nodes_list) - n

        if node_to_remove == 0:
            if len(nodes_list) > 1:
                return nodes_list[1]
            else:
                return None

        else:
            if node_to_remove+1 < len(nodes_list):
                nodes_list[node_to_remove-1].next = nodes_list[node_to_remove+1]
            else:
                nodes_list[node_to_remove-1].next = None
            return head
        