class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        counter = 0
        from collections import defaultdict
        hm = defaultdict(list)

        for i in range (0, len(isConnected)):
            elements = isConnected[i]
            for j in range(0, len(isConnected)):
                if isConnected[i][j] == 1:
                    hm[i].append(j)
                    # hm[j].append(i)
                    

        visited = [0] * (len(isConnected))

        def recurse(node, visited):
            if visited[node] == 1:
                return

            visited[node] = 1

            elements = hm[node]

            for i in range (0 , len(elements)):
                if visited[elements[i]] == 0:
                    recurse(elements[i], visited)

        
        for i in range (0, len(visited)):

            if visited[i] == 0:
                counter += 1
                recurse(i, visited)
        # print(hm)
        return counter