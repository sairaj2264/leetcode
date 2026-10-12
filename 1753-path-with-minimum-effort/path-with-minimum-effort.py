class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        import heapq
        from collections import defaultdict
        n = len(heights)
        m = len(heights[0])
        distance = [[1000001] *m for _ in range(n)]
        dx = [-1,0,0,1]
        dy = [0,-1,1,0]
        heap = []
        distance[0][0] = 0
        heapq.heappush(heap, (0,0,0))

        length = 0

        while(len(heap) > 0):
            dist, x, y = heapq.heappop(heap)
            if x == (n - 1) and y == (m - 1):
                length = dist
                break
            for i in range(0 , len(dx)):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                    temp = abs(heights[new_x][new_y] - heights[x][y])
                    new_effort = max(dist,temp)
                    if new_effort < distance[new_x][new_y]:
                        distance[new_x][new_y] = new_effort
                        heapq.heappush(heap, (new_effort,new_x, new_y))

        return length

                    

        

        