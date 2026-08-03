# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        def recurseLeft(root, height):

            if root is None:
                return height

            return recurseLeft(root.left, height + 1)

        # print(recurseLeft(root, 0))
        # return 0

        def recurseRight(root, height):

            if root is None:
                return height

            return recurseRight(root.right, height + 1)
            
        # print(recurseRight(root, 0))

        def recurse(root):

            if root is None:
                return 0
            l = recurseLeft(root, 0)
            r = recurseRight(root, 0)

            if l == r:
                return (1 << l) - 1

                return temp            
            return (1 + recurse(root.left) + recurse(root.right))

        ans = recurse(root)
        if ans <= 0:
            return 1

        return ans

        