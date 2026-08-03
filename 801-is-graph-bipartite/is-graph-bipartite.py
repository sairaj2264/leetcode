class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        visited = [0] * 101
        partition = [-1] * 101


        q = deque()

        switch = 1
        arr = 0
        for k in range(0 , len(graph)):
            arr = graph[k]
            if len(arr) == 0:
                continue
            else:
                for l in range(0 , len(arr)):
                    if visited[arr[l]] == 0:
                        q.append((arr[l],switch))

        # for j in range(0 , len(arr)):
        #     q.append((arr[j], switch))
        
        
            while(len(q) > 0):
                element = q.popleft()
                print(element)
                value = element[0]
                part = element[1]

                if visited[value] == 0:
                    visited[value] = 1
                    partition[value] = part

                elif visited[value] == 1 and partition[value] == part:
                    continue
                
                else:
                    return False


                temp = graph[value]
                if len(temp) == 0:
                    continue
                for j in range(0, len(temp)):

                    if visited[temp[j]] == 0:
                        if part == 0:
                            switch = 1
                        else:
                            switch = 0
                        q.append((temp[j], switch))


        return True
        

        