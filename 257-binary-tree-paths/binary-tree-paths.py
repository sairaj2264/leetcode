class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        if root is None:
            return []

        answer = []

        def recurse(node, arr):

            arr.append(node)

            if node.left is None and node.right is None:
                answer.append(arr.copy())
                arr.pop()
                return

            if node.left:
                recurse(node.left, arr)

            if node.right:
                recurse(node.right, arr)

            arr.pop()

        recurse(root, [])

        final_answer = []

        for arr in answer:
            ans = []
            for i in arr:
                ans.append(str(i.val))
                ans.append("->")

            ans.pop()
            ans = "".join(ans)
            final_answer.append(ans)

        return final_answer