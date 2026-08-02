# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict
        from collections import deque

        q = deque()
        hm = defaultdict(list)
        def bfs(root):

            if root is None:
                return

            if root.left is not None:
                hm[root.val].append(root.left.val)
                hm[root.left.val].append(root.val)
            
            if root.right is not None:
                hm[root.val].append(root.right.val)
                hm[root.right.val].append(root.val)

            bfs(root.left)
            bfs(root.right)

        bfs(root)
        print(hm)

        visited = [0] * 501


        q.append(target.val)
        # visited[target.val] = 1

        distance = 0
        while(len(q) > 0):

            if distance == k:
                break
            temp = len(q)
            for i in range(0 , temp):
                element = q.popleft()
                if visited[element] == 0:
                    visited[element] = 1

                    values = hm[element]
                    for j in range(0 , len(values)):
                        if visited[values[j]] == 0:
                            q.append(values[j])
            distance += 1


        ans = []
        while(len(q) > 0):
            element = q.popleft()
            ans.append(element)

        return ans



        # before_stack = []
        # after_stack = []

        # idx = 0

        # def traverse(root, depth, found, target, before_stack, after_stack):
        #     nonlocal idx
        #     if root is None:
        #         return
        #     elif found == True:
        #         after_stack.append((depth, root.val))
        #     elif found == False:
        #         if root == target:
        #             idx = depth
        #             found = True
        #         else:
        #             before_stack.append((depth, root.val))
                    
        #     traverse(root.left, depth + 1, found, target, before_stack, after_stack)
        #     traverse(root.right, depth + 1, found, target, before_stack, after_stack)

        
        # traverse(root, 0, False, target, before_stack, after_stack)
        # # print(before_stack)
        # # print(after_stack)
        # # print(idx)

        # counter = 0
        # answer = []
        # flag = False
        # print(before_stack)
        # # before_stack = before_stack[:: -1]
        # # print(before_stack)
        # while(len(before_stack) > 0):

        #     element = before_stack.pop()
            
        #     if element[0] == 0:
        #         flag = True
        #     if flag == False:
        #         if (idx - element[0]) == k:
        #             counter += 1
        #             answer.append(element[1])
        #     if flag == True:
        #         if (element[0] + idx) == k:
        #             counter += 1
        #             answer.append(element[1])

        # while(len(after_stack) > 0):
        #     # print(element[0] - idx)
        #     element = after_stack.pop()
        #     if (element[0] - idx) == k:
        #         counter += 1
        #         answer.append(element[1])

        # return answer       