class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        visited = [-1] * (n)

        # print(visited)

        answer = []
        def dfs(graph, visited, answer, idx):

            if graph[idx] == []:
                if visited[idx] != 1:
                    visited[idx] = 1
                    answer.append(idx)
                return 1

            if visited[idx] == 1:
                return 1
            if visited[idx] == 0:
                return 0

            visited[idx] = 0
            anss = 1

            elements = graph[idx]
            for i in range(0 , len(elements)):
                if visited[elements[i]] == -1:
                    flag = dfs(graph, visited, answer, elements[i])
                    if flag == 0:
                        anss = 0
                
                elif visited[elements[i]] == 0:
                    anss = 0
                    break

            if anss == 0:
                return 0
            else:
                visited[idx] = 1
                answer.append(idx)
                return 1





        for i in range(0 , len(visited)):
            if visited[i] == -1:    
                ans = dfs(graph, visited, answer, i)
        
        answer.sort()
        return answer