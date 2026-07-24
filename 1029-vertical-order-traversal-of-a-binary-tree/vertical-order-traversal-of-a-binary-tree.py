# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        answer = []

        hm = defaultdict(list)
        def recurse(root,x,y,added):
            
            temp = []
            if added == False:
                added = True
                hm[x].append([root.val,y])

            if root.left is not None:
                recurse(root.left,x - 1,y + 1, False)

            if root.right is not None:
                recurse(root.right, x + 1,y + 1, False)

        recurse(root,0,0,False)
        hm = defaultdict(list,sorted(hm.items()))


        for key in hm:
            hm[key].sort(key = lambda x: (x[1], x[0]))
        for key in hm:
            temp = hm[key]
            temp1 = []
            for i in temp:
                temp1.append(i[0])
            answer.append(temp1)

            print(key, temp)

            # answer.append(temp)

        return answer
                
            
        