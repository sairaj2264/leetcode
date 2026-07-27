# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse(root):
            if root is None:
                return None

            if root.val == p.val:
                return root
            
            elif root.val == q.val:
                return root

            left = recurse(root.left)
            right = recurse(root.right)

            if left is None and right is None:
                return None
            
            elif left is None and right is not None:
                return right
            
            elif left is not None and right is None:
                return left
            
            elif left is not None and right is not None:
                return root

        answer = recurse(root)
        return answer









        # hm = {}
        # found = False
        # answer = []
        # path = []
        # def recursep(node, path, answer, p):
        #     nonlocal found
        #     if found == True:
        #         return
        #     if node is None:
        #         return
        #     path.append(node)

        #     if  node.val == p.val:
        #         answer.append(path.copy())
        #         found = True
        #         return

        #     if found == False:
        #         recursep(node.left, path, answer,p)
        #         recursep(node.right, path, answer, p)
        #         path.pop()


        # recursep(root, path, answer, p)
        # path = []
        # found = False
        # recursep(root, path, answer, q)
        # print(answer)

        # i = 0
        # j = 0
        # temp = 0
        # while (i < len(answer[0]) and j < len(answer[1])):

        #     if answer[0][i].val == answer[1][j].val:
        #         temp = answer[0][i]
        #     else:
        #         break

        #     i += 1
        #     j += 1
        
        
            
        # return temp







        