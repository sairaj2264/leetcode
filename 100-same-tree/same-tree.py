# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        arr1 = []
        arr2 = []

        def recurse(root, arr):

            if root is None:
                arr.append('')
                return
            
            recurse(root.left, arr)
            recurse(root.right, arr)

            arr.append(root.val)


        recurse(p, arr1)
        recurse(q, arr2)
        # print(arr1)
        # print(arr2)
        
        if len(arr1) != len(arr2):
            return False

        for i in range (0, len(arr1)):
            if arr1[i] != arr2[i]:
                return False

        return True
        