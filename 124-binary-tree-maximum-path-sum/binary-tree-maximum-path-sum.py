# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxx = float('-inf')

        if root.left is None and root.right is None:
            return root.val

        def recurse(root):

            nonlocal maxx
            if root is None:
                return float('-inf')

            left = float('-inf')    
            right = float('-inf')
            if root.left is not None:
                left = recurse(root.left)
            if root.right is not None:
                right = recurse(root.right)


            left_sum = left + root.val
            right_sum = right + root.val
            total_sum = left_sum + right_sum - root.val

            maxx = max(total_sum,root.val, left_sum , right_sum, maxx)

            return max(root.val, left_sum, right_sum)


            # if left is float('-inf') and right is float('-inf'):
            #     maxx = max(maxx, root.val)
            #     return root.val

            # temp1 = float('-inf')
            # temp2 = float('-inf')

            # maxx = max(root.val, maxx)
            # if left is not None:
            #     temp1 = left + root.val
            # if right is not None:
            #     temp2 = right + root.val

            # maxx = max((temp1 + temp2 - root.val),temp1, temp2, maxx)
            # temp = max(temp1, temp2, maxx)
            # if temp < 0:
            #     return 0

        recurse(root)
        return maxx



        