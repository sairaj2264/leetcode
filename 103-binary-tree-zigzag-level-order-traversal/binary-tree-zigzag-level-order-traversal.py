# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque
        flag = True
        q = deque()
        ans = []
        if root is None:
            return([])
        q.append(root)


        # start = True
        count = 0
        while (len(q) > 0):
            
            temp = []
            lenn = len(q)
            k = 0
            while (k < lenn):
                element = q.popleft()
                temp.append(element.val)
                if element.left is not None:
                    q.append(element.left)
                if element.right is not None:
                    q.append(element.right)
                k+=1

            temp1 = []
            for i in range (0 , len(temp)):
                if flag == True:
                    temp1.append(temp[i])
                else:
                    temp1.append(temp[len(temp) - 1 - i])

            ans.append(temp1)
            flag = not flag
                
        return ans

            
    
        # def recurse(root, temp):

        #     if root is None:
        #         return

        #     if temp == True:

        #         if root.left is not None and root.right is None:
        #             ans.append([root.left.val])

        #         if root.left is None and root.right is not None:
        #             ans.append([root.right.val])

        #         if root.left is not None and root.right is not None:
        #             ans.append([root.left.val, root.right.val])

        #         recurse(root.left, False)
        #         recurse(root.right, False)

        #     else:

        #         if root.left is None and root.right is not None:
        #             ans.append([root.right.val])

        #         if root.left is not None and root.right is None:
        #             ans.append([root.left.val])



        #         if root.left is not None and root.right is not None:
        #             ans.append([ root.right.val, root.left.val])

        #         recurse(root.right, True)
        #         recurse(root.left, True)

        # recurse(root, False)
        # return ans


        # while (len(stack) > 0):
            
        #     element = stack.pop()


                
        #     if temp == True:




        #         if element.left is not None:
        #             stack.append(element.left)
        #         if element.right is not None:
        #             stack.append(element.right)


        #             ans.append([element.right.val,  element.left.val])

        #         temp = False
        #     else:

        #         if element.right is not None:
        #             stack.append(element.right)

        #         if element.left is not None:
        #             stack.append(element.left)




        #             ans.append([element.left.val,  element.right.val])

        #         temp = True

        # return ans

        
        