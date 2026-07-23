class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        arr1 = []
        arr2 = []
        
        def counter(nums, arr):
            for i in range (0, 32):
                temp = nums >> i
                ans = temp & 1
                arr.append(ans)

        counter(start, arr1)
        counter (goal, arr2)

        answer = 0
        for i in range (0 , 32):
            if arr1[i] != arr2[i]:
                answer += 1

        return answer
            