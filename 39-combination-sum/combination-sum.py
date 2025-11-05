class Solution(object):


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def combSum(i,arr,summ):
            if i >= len(candidates):
                return
            if summ == target:
                ans.append(list(arr))
                return
            if summ < target:
                arr.append(candidates[i])
                summ += candidates[i]
                combSum(i,arr,summ)

                arr.pop()
                summ -= candidates[i]
                combSum(i+1,arr,summ)



        ans = []
        arr = []
        combSum(0,arr,0)
        return ans


        