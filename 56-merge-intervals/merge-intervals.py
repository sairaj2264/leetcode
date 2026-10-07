class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()

        start = None
        end = None
        answer = []

        for i in range(0 , len(intervals)):
            if start is None:
                start = intervals[i][0]
                end = intervals[i][1]
                continue
            new_start = intervals[i][0]
            new_end = intervals[i][1]

            if new_start <= end:
                end = max(end, new_end)
            else:
                answer.append([start, end])
                start = new_start
                end = new_end
        answer.append([start, end])
        return answer
            
        