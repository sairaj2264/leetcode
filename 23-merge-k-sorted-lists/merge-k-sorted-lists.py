# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        import heapq
        heap = []
        for i in range(0 , len(lists)):

            elements = lists[i]
            if elements == []:
                continue
            root = elements

            while (1):
                if root is None:
                    break
                heapq.heappush(heap, root.val)
                root = root.next

        # print(heap)
        root = None
        first = None

        if len(heap) == 1:
            return ListNode(heap.pop())
        while (len(heap) > 0):
            if root is None:
                root = ListNode(heapq.heappop(heap))
                first = root
            element = ListNode(heapq.heappop(heap))
            root.next = element
            root = element

        return first

        