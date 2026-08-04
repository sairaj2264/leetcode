# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:



        
        def recurse(inorder, preorder):
            
            if len(inorder) == 0 or len(preorder) == 0:
                return None

            root = TreeNode(preorder[0])
            old_inorder = []
            new_inorder = []
            flag = False
            count = 0
            for i in range(0 , len(inorder)):
                if inorder[i] == preorder[0]:
                    flag = True
                    count += 1
                    continue
                elif flag == False:
                    old_inorder.append(inorder[i])
                    count += 1
                else:
                    new_inorder.append(inorder[i])

             
            new_preorder = []
            old_preorder = []
            

            for i in range(0, len(preorder)):
                if preorder[i] == preorder[0]:
                    continue
                    

                elif i <= (count - 1):
                    old_preorder.append(preorder[i])
                
                else:
                    new_preorder.append(preorder[i])

            root.left = recurse(old_inorder, old_preorder) 
            root.right = recurse(new_inorder, new_preorder)

            return root
            
            
        answer = recurse(inorder, preorder)
        return answer
        