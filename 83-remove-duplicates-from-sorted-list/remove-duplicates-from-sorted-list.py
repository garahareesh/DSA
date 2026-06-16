# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = set()
        temp_node = head
        prev = None
        while temp_node:
            if temp_node.val in temp:
                prev.next = temp_node.next
            else:
                temp.add(temp_node.val)
                prev = temp_node
            temp_node =temp_node.next
        return head
        