# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        if root.left is not None:
            if root.right is None:
                return False

        if root.right is not None:
            if root.left is None:
                return False
        answerLeft = []
        answerRight = []
        def recurseLeft(root, pos,dirr, answerLeft):
            if root is None:
                return
            answerLeft.append((root.val, abs(pos), dirr))
            recurseLeft(root.left, pos - 1,'l', answerLeft)
            recurseLeft(root.right, pos + 1,'r', answerLeft)


        def recurseRight(root, pos,dir, answerRight):
            if root is None:
                return
            answerRight.append((root.val, abs(pos), dir))
            
            recurseRight(root.right, pos + 1,'r', answerRight)
            recurseRight(root.left, pos - 1,'l', answerRight)

        recurseLeft(root, 0 ,'l', answerLeft)
        recurseRight(root, 0,'r', answerRight)
        print(answerLeft)
        print(answerRight)
        if len(answerLeft) == len(answerRight):
            for i in range (0 , len(answerRight)):
                if answerLeft[i][0] != answerRight[i][0] or answerLeft [i][1] != answerRight[i][1] or answerLeft[i][2] == answerRight[i][2]:
                    return False

        return True


