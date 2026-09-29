# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        temp = head

        count = 1
        first_odd = ListNode(None)
        last_odd = ListNode(None)
        first_even = ListNode(None)

        while temp is not None:
            next_temp = temp.next
            if count%2 == 1:
                if first_odd.val == None:
                    first_odd = temp
                
                if temp.next is not None:
                    temp.next = temp.next.next
                    last_odd = temp
                else:
                    temp.next = None
            
            else:
                if first_even.val == None:
                    first_even = temp

                if temp.next is not None:
                    temp.next = temp.next.next
                else:
                    temp.next = None

            temp = next_temp
            count += 1


        if last_odd.next is not None:
            last_odd = last_odd.next
        last_odd.next = first_even

        return head
        
        