class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict, deque

        adj = defaultdict(list)
        q = deque()


        visited = n * [10000000]
        for source, connection, distance in flights:
            adj[source].append((connection, distance))

        q.append((0,k+1,src))
        answer = float('inf')
        visited[src] = 0
        while len(q) > 0:
            # print(q)

            dist, k, node = q.popleft()
            if node == dst:
                answer = min(dist, answer)
                visited[dst] = min(dist, answer)
            
            k-= 1

            if k >= 0:
                nodes = adj[node]
                for connection, length in nodes:
                    new_distance = length + dist
                    if visited[connection] >= new_distance:
                        q.append((new_distance, k, connection))
                        visited[connection] = new_distance

        if answer == float('inf'):
            return -1
        return answer

        