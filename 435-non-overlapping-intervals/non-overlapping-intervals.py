class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[1])

        # print(intervals)

        count = 1
        temp = intervals[0][1]
        for i in range(1, len(intervals)):
            if temp <= intervals[i][0]:
                temp = intervals[i][1]
                count +=1
        return ( len(intervals) - count )




        # nums = []
        # arr= [0] * 100001

        # for i in range (0, len(intervals)):
        #     temp = (intervals[i][0], intervals[i][1], intervals[i][1] - intervals[i][0])
        #     nums.append(temp)

        # nums.sort(key = lambda x:( x[2] ))

        # print(intervals)
        # count = 0
        # for i in range (0, len(nums)):
        #     if arr[nums[i][0]] != 1:
        #         for j in range (nums[i][0], nums[i][1]):
        #             arr[j] = 1
        #     else:
        #         count += 1
        # return count
                     

        



        