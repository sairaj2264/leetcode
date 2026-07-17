class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        arr = []
        i = 0
        while ( i < len(intervals) and intervals[i][1] < newInterval[0]):
            arr.append(intervals[i])
            i += 1

        while (i < len(intervals) and intervals [i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0], newInterval[0] )
            newInterval[1] = max(intervals[i][1], newInterval[1] )
            i += 1

        arr.append(newInterval)

        while i < len(intervals):
            arr.append(intervals[i])
            i += 1

        return arr

#         nums = intervals.copy()
#         arr = []
#         answerIdx = -1
#         loww = 0  
#         high = 0 
#         flag1 = False
#         flag2 = False
#         for i in range (0, len(intervals)):

#             if nums[i][0] <= newInterval[0] and nums[i][1] >= newInterval[1]:
#                 loww = newInterval[0]
#                 high = newInterval[1]
#                 flag1 = True
#                 flag2 = True
#                 answerIdx = i
#                 arr.append([loww, high])
#                 continue

#             if flag1 == False and nums[i][0] <= newInterval[0] and nums[i][1] > newInterval[0]:
#                 loww = nums[i][0]
#                 flag1 = True
#                 answerIdx = i
#                 arr.append([loww, high])
#                 continue

            
#             if flag2 == False and nums[i][1] >= newInterval[1] and nums[i][0] <= newInterval[1]:
#                 high = nums[i][1]
#                 flag2 = True

#                 if flag1 == True:
#                     arr[answerIdx][1] = high
#                 else:
#                     answerIdx = i
#                     arr.append([loww, high])
#                 continue
            
#             if nums[i][0] > newInterval[0] and nums[i][1] < newInterval[1]: 
#                 continue

#             arr.append([nums[i][0], nums[i][1]])

#         if flag1 == False and flag2 == False:

#             if intervals[0][0] < newInterval:
#                 return [intervals]
#             else:
#                 return [newInterval]
#         if flag1 == False:
#             arr[answerIdx][0] = newInterval[0]

        
#         if flag2 == False:
#             arr[answerIdx][1] = newInterval[1]
        

#         return arr


