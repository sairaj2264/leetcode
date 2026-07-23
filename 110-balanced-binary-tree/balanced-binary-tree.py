# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recurse(root , ans):

            if root is None:
                return 0

            left = 1 + recurse(root.left , ans)
            right = 1 + recurse(root.right , ans)

            if(abs(left-right)>1):
                ans[0] = False

            return max(left,right)

        if root is None:
            return True

        ans = [True]
        recurse(root,ans)

        return ans[0]

