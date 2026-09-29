class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        temp = head

        if temp is None:
            return None

        if temp.next is None:
            return None

        count = 0

        while temp is not None and count < n:
            temp = temp.next
            count += 1

        if temp is None:
            return head.next

        slow = head

        while temp.next is not None:
            temp = temp.next
            slow = slow.next

        del_node = slow.next
        slow.next = del_node.next
        del_node.next = None

        return head