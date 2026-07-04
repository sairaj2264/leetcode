class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        answer = []
        temp = []
        def combiSum(arr, n, target, temp, counter, summ, answer):
            if counter == n:
                if summ == target:    
                    answer.append(temp[:])
                    return
                return

            if summ > target or counter > n:
                return
            if counter < n:
                temp.append(arr[counter])
                summ += arr[counter]

            combiSum (arr,n,target,temp,counter,summ, answer)
            summ -= arr[counter]
            temp.pop()
            combiSum (arr,n,target,temp,counter + 1,summ, answer)
            return
        combiSum(candidates, n, target, temp, 0, 0, answer)
        return answer


        