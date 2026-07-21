# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

        q = deque()
        answer = []

        if root is None:
            return answer

        else:
            q.append(root)

        while (len(q) > 0):

            temp = []
            tempNode = 0
            n = len(q)
            for i in range (0, n):
                tempNode = q.popleft()
                temp.append(tempNode.val)
                if tempNode.left is not None:
                    q.append(tempNode.left)
                if tempNode.right is not None:
                    q.append(tempNode.right)
            answer.append(temp)
            
        return answer
                
                     
        