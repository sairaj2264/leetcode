class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def lower_bound(element):
            i = 0
            j = len(arr) - 1

            answer = -1
            while i <= j:
                mid = (i + j)//2
                if arr[mid] >= element:
                    answer = mid
                    j = mid - 1
                else:
                    i = mid + 1
            return answer


        arr = []
        arr.append(nums[0])
        for i in range(1 , len(nums)):
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                index = lower_bound(nums[i])
                arr[index] = nums[i]
        print(arr)
        return len(arr)



        # dp = [[-1] *(len(nums) +1) for _ in range(len(nums))]
        # def recurse(i,prev):

        #     if i >= len(nums):
        #         return 0
            
        #     if dp[i][prev+1] != -1:
        #         return dp[i][prev+1]

        #     if prev == -1:
        #         ans1 = 1 + recurse(i+1, i)
        #         ans2 = recurse(i+1, prev)
        #         dp[i][prev + 1] = max(ans1, ans2)
        #         return dp[i][prev + 1]
        #     elif prev != -1 :
        #         if nums[i] > nums[prev]:
        #             ans1 = 1 + recurse(i+1, i)
        #             ans2 = recurse(i+1, prev)
        #             dp[i][prev+1] = max(ans1, ans2)
        #             return dp[i][prev+1]

        #         else:
        #             dp[i][prev + 1] = recurse(i+1, prev)
        #             return dp[i][prev + 1]
        
        # return recurse(0,-1)

        