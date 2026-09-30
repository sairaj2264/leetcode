# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        answer = None
        if temp1 is None or temp2 is None:
            return answer
        FLAG = 0
        while FLAG < 3:
            if temp1 == temp2:
                answer = temp2
                break

            else:
                temp1 = temp1.next
                temp2 = temp2.next

                if temp1 == None:
                    temp1 = headB
                    FLAG += 1
                if temp2 == None:
                    temp2 = headA
                    FLAG += 1

        return answer