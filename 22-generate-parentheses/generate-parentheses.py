class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []
        arr = []
        def generatePara(openUse, closeUse, arr, n):
            if openUse == closeUse and closeUse == n:
                answer.append("".join(arr))
                return

            if openUse < n:
                arr.append("(")
                generatePara(openUse + 1, closeUse, arr, n)
                arr.pop()

            
            if closeUse < openUse:
                arr.append(")")
                generatePara(openUse, closeUse + 1, arr, n)
                arr.pop()
            
        generatePara(0,0,arr,n)
        return answer
