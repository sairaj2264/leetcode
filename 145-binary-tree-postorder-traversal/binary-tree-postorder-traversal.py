# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # answer = []

        # def traverse(node):

        #     if node is None:
        #         return

        #     traverse(node.left)
        #     traverse(node.right)
        #     answer.append(node.val)

        # traverse(root)
        # return answer

        if root is None:
            return([])
        stack = []

        preOrder = []
        inOrder = []
        postOrder = []



        stack.append([root, 1])

        while (len(stack) > 0):

            temp = stack.pop()
            if temp[1] == 1:
                preOrder.append(temp[0].val)
                temp[1] += 1
                stack.append(temp)
                if temp[0].left is not None:
                    stack.append([temp[0].left,1])
            elif temp[1] == 2:
                inOrder.append(temp[0].val)
                temp[1] += 1
                stack.append(temp)
                if temp[0].right is not None:
                    stack.append([temp[0].right, 1])

            else:
                postOrder.append(temp[0].val)

        print(preOrder)
        print(inOrder)
        return(postOrder)
        