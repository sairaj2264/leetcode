class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def calculate_distance(a,b):
            a_s = a * a
            b_s = b * b
            total = a_s + b_s
            return total

        import heapq
        heap = []

        for i in range (0 , len(points)):
            a,b = points[i]
            dist = calculate_distance(a,b)
            heapq.heappush(heap,(dist, (a,b)))
        ans = []
        while k > 0:
            dist, [a, b] = heapq.heappop(heap)
            ans.append([a,b])
            k -= 1
        return ans
