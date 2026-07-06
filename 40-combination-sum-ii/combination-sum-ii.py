class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        temp = []
        answer = []
        n = len(candidates)
        candidates.sort()
        def combiSum2(nums, n, target, counter, tempSum, tempArr, answer):
            if tempSum == target:
                answer.append(tempArr[:])
            elif tempSum > target:
                return

            for i in range(counter,n):
                if i != counter and nums[i] == nums[i-1]:
                    continue
                tempSum += nums[i]
                tempArr.append(nums[i])
                combiSum2(nums, n, target, i + 1,tempSum, tempArr, answer)
                tempSum -= nums[i]
                tempArr.pop()
        
        combiSum2(candidates, n, target, 0,0, temp, answer)
        return answer
