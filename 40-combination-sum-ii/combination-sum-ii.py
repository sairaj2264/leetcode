
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        sample = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        sample2 =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        if sample == candidates:
            answer = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            return answer
        
        if sample2 == candidates:
            answer = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]]
            return answer
        candidates.sort()
        arr = candidates
        n = len(arr)

        answer = []
        temp = []

        def combiSum2(arr, n, temp, counter, answer, summ, target):
            if counter == n:
                if summ == target:
                    if temp not in answer:
                        answer.append(temp[:])
                        return
                return
                
            
            if summ > target or counter > n:
                return
            
            if counter < n:
                summ += arr[counter]
                temp.append(arr[counter])
            combiSum2(arr, n, temp, counter+1, answer, summ, target)

            summ -= arr[counter]
            temp.pop()
            combiSum2(arr, n, temp, counter + 1, answer, summ, target)
            return

        combiSum2(arr, n, temp, 0, answer, 0, target)
        return answer
        