class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        arr = [1,2,3,4,5,6,7,8,9]
        tempArr= []
        tempSum = 0
        targetIndex = k
        targetSum = n
        answer = []


        def combiSum3(arr,targetIndex, targetSum, tempArr, tempSum,counter, answer):
            if len(tempArr) == targetIndex and tempSum == targetSum:
                answer.append(tempArr[:])
                return
            
            elif len(tempArr) > targetIndex or tempSum > targetSum or counter > 8:
                return

            tempSum += arr[counter]
            tempArr.append(arr[counter])
            combiSum3(arr,targetIndex, targetSum, tempArr, tempSum,counter + 1, answer)
            tempSum -= arr[counter]
            tempArr.pop()
            combiSum3(arr,targetIndex, targetSum, tempArr, tempSum,counter + 1, answer)

        
        combiSum3(arr,targetIndex, targetSum, tempArr, tempSum, 0 , answer)
        return answer