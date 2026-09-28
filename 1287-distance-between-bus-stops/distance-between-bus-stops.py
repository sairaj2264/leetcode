class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        total_distance = 0

        for i in distance:
            total_distance += i

        p1 = min(start, destination)
        p2 = max(start, destination)

        sum1 = 0
        for i in range (p1, p2):
            sum1 += distance[i]

        sum2 = total_distance - sum1

        answer = min(sum1, sum2)

        return answer