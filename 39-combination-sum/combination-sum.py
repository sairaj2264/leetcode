class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def combi_sum(i,temp,val,answer,candidates):
            if i >= len(candidates):
                return

            if val == target:
                answer.append(temp.copy())
                temp = []
                return

            if val < target:
                temp.append(candidates[i])
                val += candidates[i]
                combi_sum(i, temp, val, answer, candidates)
                temp.pop()
                val -= candidates[i]
                combi_sum(i+1, temp, val, answer, candidates)

        temp = []
        answer = []
        combi_sum(0,temp,0,answer, candidates)
        return answer

            

        