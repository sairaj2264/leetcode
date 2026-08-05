# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []

        current = root

        while current is not None:

            if current.left is not None:
                prev = current.left

                while prev.right is not None and prev.right is not current:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = current
                    answer.append(current.val)
                    current = current.left
                else:
                    current = current.right
            
            else:
                answer.append(current.val)
                current = current.right

        return answer


        # def traverse(node):

        #     if node is None:
        #         return

        #     answer.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)

        # traverse(root)

        # return answer