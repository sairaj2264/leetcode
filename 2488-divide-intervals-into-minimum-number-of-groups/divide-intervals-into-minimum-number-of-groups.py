class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        arrival = []
        departure = []

        for i in range(len(intervals)):
            arrival.append(intervals[i][0])
            departure.append(intervals[i][1])
        
        arrival.sort()
        departure.sort()

        count = 0
        i = 0
        j = 0
        answer = 0
        while(i<len(arrival) and j < len(departure)):
            if arrival[i] <= departure[j]:
                count += 1
                answer = max(answer, count)
                i += 1
            else:
                count -= 1
                j += 1

        if len(intervals) > 0 and answer == 0:
            answer = 1
        return answer
        