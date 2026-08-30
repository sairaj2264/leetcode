class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        hm = {}
        prev = 100000
        answer = 0
        for i in range(0 , len(nums)):
            
            if nums[i] != prev:
                if hm.get(nums[i],0) > 0:
                    temp = hm.get(nums[i],0)
                    if temp%2 != 0:
                        answer -=1
                        hm[nums[i]] = 2
                    prev = nums[i]
                else:
                    hm[nums[i]] = 1
                    prev = nums[i]
                    answer += 1

        print(hm)
        return answer

        