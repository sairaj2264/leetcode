# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nodes = []

        temp = head

        if head is None:
            return None
        while temp is not None:
            nodes.append(temp)
            temp = temp.next
        
        m = len(nodes)
        temp = nodes[m - 1]
        new_head = temp
        nodes.pop()
        while len(nodes) > 0:
            element = nodes.pop()
            temp.next = element
            temp = element

        temp.next = None

        return new_head


        