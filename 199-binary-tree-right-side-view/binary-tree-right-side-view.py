# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque
        q = deque()
        hm = {}
        if root is None:
            return []
        q.append((root, 0))

        while (len(q) > 0):
            element = q.popleft()
            root = element[0]
            height = element[1]

            hm[height] = root.val
            if root.left is not None:
                q.append((root.left, height + 1))
            
            if root.right is not None:
                q.append((root.right, height + 1))
        
        answer = []
        hm = dict(sorted(hm.items()))
        for key in hm:
            answer.append(hm[key])

        return answer
        