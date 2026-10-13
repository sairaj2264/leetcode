class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq

        heap = []
        adj = defaultdict(list)
        for time in times:
            source, target, wt = time
            source -= 1
            target -= 1
            adj[source].append((target, wt))

        distance_arr = [1000000] * n

        distance_arr[k-1] = 0
        heapq.heappush(heap, (0, k-1))

        while ( len(heap) > 0):
            time, node = heapq.heappop(heap)
            connections = adj[node]

            for connection in connections:
                target , wt = connection
                total_time = time + wt
                if total_time < distance_arr[target]:
                    distance_arr[target] = total_time
                    heapq.heappush(heap, (total_time, target))
        answer_time = 0

        for i in distance_arr:
            if i == 1000000:
                answer_time = -1
                break
            answer_time = max(answer_time, i)

        return answer_time
