# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        if root is None:
            return arr

        def recurse(root):
            if root is None:
                return

            arr.append(root)
            recurse(root.left)
            recurse(root.right)

        recurse(root)
        for i in range(len(arr)):
            arr[i].left = None
            if i+1 < len(arr):
                arr[i].right = arr[i+1]
            else:
                arr[i].right = None

        return arr[0]