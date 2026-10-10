class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict

        adj = defaultdict(list)
        for i in range(0 , len(prerequisites)):
            a,b = prerequisites[i]
            adj[b].append(a)

        visited = [-1] * (numCourses)
        path_visited = [-1] * (numCourses)
        answer = True

        def dfs(node, visited, path_visited):
            if path_visited[node] == 1:
                return True
            if visited[node] == 1:
                return False

            visited[node] = 1
            path_visited[node] = 1

            elements = adj[node]

            for i in elements:
                temp = dfs(i, visited, path_visited)
                if temp == True:
                    return True
            
            path_visited[node] = -1
            return False



        for i in range(0,len(visited)):
            if visited[i] == -1:
                temp = dfs(i, visited, path_visited)
                if temp == True:
                    answer = False
                    break
                

        return answer

        