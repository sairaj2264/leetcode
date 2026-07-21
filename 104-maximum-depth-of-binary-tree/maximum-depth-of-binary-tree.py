# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        maxx = 1

        def traverse(node, counter):
            nonlocal maxx
            if node.left is not None:
                maxx = max(maxx, counter)
                traverse(node.left, counter + 1)
            
            if node.right is not None:
                maxx = max(maxx, counter)
                traverse(node.right, counter + 1)

            return

        traverse(root, 2)
        return maxx