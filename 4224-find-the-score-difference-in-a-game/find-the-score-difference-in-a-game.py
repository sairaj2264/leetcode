class Solution:
    def scoreDifference(self, nums: List[int]) -> int:

        counter1 = 0
        counter2 = 0
        temp = True
        i = 0
        while (i < len(nums)):
            if ((i+1)%6 == 0):
                temp = not temp
            
            if nums[i] % 2 == 1:
                temp = not temp

            if temp == True:
                counter1 += nums[i]
            else:
                counter2 += nums[i]
            
            i+=1
        
        answer = counter1 - counter2
        return answer
                 

        # return 1
        