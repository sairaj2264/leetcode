class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        from collections import defaultdict
        import heapq

        adj = defaultdict(list)
        answer_threshold = 1000000
        answer_node = float('-inf')
        for edge in edges:
            source, target, weight = edge
            adj[source].append((target, weight))
            adj[target].append((source, weight))


        for i in range(0 , n):
            rechable_cities = 0
            distance_arr = [1000000]*n
            heap = []
            distance_arr[i] = 0
            heapq.heappush(heap, (0 , i))

            while len(heap) > 0:
                distance, source = heapq.heappop(heap)
                connected_nodes = adj[source]
                for connection in connected_nodes:
                    node, connection_dist = connection
                    new_distance = distance + connection_dist
                    if new_distance < distance_arr[node]:
                        distance_arr[node] = new_distance
                        if distance_arr[node] <= distanceThreshold:
                            heapq.heappush(heap,(new_distance, node)) 
            for j in distance_arr:
                if j <= distanceThreshold:
                    rechable_cities += 1
            rechable_cities -= 1
            if rechable_cities <= answer_threshold:
                answer_threshold = rechable_cities
                answer_node = i

        return answer_node
