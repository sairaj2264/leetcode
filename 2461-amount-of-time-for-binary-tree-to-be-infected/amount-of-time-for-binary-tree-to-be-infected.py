# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        from collections import defaultdict
        from collections import deque

        hm = defaultdict(list)
        q = deque()
        visited = [0] * 100001

        def dfs(root):

            if root is None:
                return
            
            if root.left is not None:
                hm[root.val].append(root.left.val)
                hm[root.left.val].append(root.val)

            if root.right is not None:
                hm[root.val].append(root.right.val)
                hm[root.right.val].append(root.val)

            dfs(root.left)
            dfs(root.right)


        dfs(root)


        print(hm)
        q.append(start)

        answer = -1
        while (len(q) > 0):            
            length = len(q)
            for i in range(0 , length):
                element = q.popleft()
                if visited[element] == 0:
                    visited[element] = 1
                    values = hm[element]

                    for j in range(0 , len(values)):
                        if visited[values[j]] == 0:
                            q.append(values[j])
            answer += 1

        return answer
                


            
