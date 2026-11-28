class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        arr = [1] * len(nums)
        index = []

        for i in range(0 , len(nums)):
            index.append(i)
        
        for i in range(1, len(nums)):

            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if arr[i] < arr[j] + 1:
                        arr[i] = arr[j] + 1
                        index[i] = j
        maxie = 0
        indexx = -1
        # print(arr)
        # print(index)
        for i in range(0 , len(nums)):
            if arr[i] > maxie:
                maxie = arr[i]
                indexx = i

        i = indexx
        j = -1
        answer = []
        while i != j:
            answer.append(nums[i])
            j = i
            i = index[i]

        answer = answer[::-1]
        return answer


        