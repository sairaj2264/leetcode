# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        #Morris In Order Traversal

        current = root

        answer = []
        while current is not None:
            if current.left is None:
                answer.append(current.val)
                current = current.right
            
            else:
                prev = current.left

                while prev.right is not None and prev.right is not current:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = current
                    current = current.left
                
                else:
                    prev.right = None
                    answer.append(current.val)
                    current = current.right

        return answer



        # print(answer)
                


        # answer = []
        # def traverse(node):

        #     if node is None:
        #         return

        #     traverse(node.left)
        #     answer.append(node.val)
        #     traverse(node.right)

        # traverse(root)
        # return answer
        