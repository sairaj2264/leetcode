class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        stack = []

        from collections import defaultdict
        hm = defaultdict(list)
        visited = [0] * numCourses

        for i in range(0 , len(prerequisites)):
            hm[prerequisites[i][1]].append(prerequisites[i][0])

        def dfs(hm, visited, element):

            if visited[element] == 1:
                return False

            if visited[element] == 2:
                return True

            visited[element] = 1
            elements = hm[element]
            for i in range(0 , len(elements)):
                ans = dfs(hm, visited, elements[i])
                if ans == False:
                    return False
            
            stack.append(element)
            visited[element] = 2
            return True
        ans = True
        for i in range(0 , len(visited)):
            if visited[i] == 0:
                ans = dfs(hm, visited, i)
                if ans == False:
                    break

        if ans == False:
            return []

        stack = stack[:: -1]
        return stack 



        
        