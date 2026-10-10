class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        from collections import deque, defaultdict
        adj = defaultdict(list)
        q = deque()
        in_degree = [0]*numCourses
        answer = []

        for i in range(0 , len(prerequisites)):
            x,y = prerequisites[i]
            adj[y].append(x)

        for key in adj:
            nodes = adj[key]
            for node in nodes:
                in_degree[node] += 1

        for i in range(0 , len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        if len(q) == 0:
            return answer

        count_operations = 0

        while (len(q) > 0):
            node = q.popleft()
            count_operations += 1
            elements = adj[node]
            for element in elements:
                in_degree[element] -= 1
                if in_degree[element] == 0:
                    q.append(element)
            if in_degree[node] == 0:
                answer.append(node)

        if count_operations < numCourses:
            return []
        else:
            return answer