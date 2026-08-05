class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        from collections import deque, defaultdict
        q = deque()
        hm = defaultdict(list)
        answerCount = 0
        in_degree = [0] * numCourses
        visited = [0] * numCourses
        # print(visited)

        for i in range (0, len(prerequisites)):
            hm[prerequisites[i][1]].append(prerequisites[i][0])
            in_degree[prerequisites[i][0]] += 1
            visited[prerequisites[i][0]] += 1


            # print(in_degree)

        for i in range(0 ,len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
                answerCount += 1
        
        while(len(q) > 0):
            # print(q)
            element = q.popleft()
            elements = hm[element]
            for i in range (0 ,len(elements)):
                in_degree[elements[i]]-=1
                if in_degree[elements[i]] == 0:
                    answerCount += 1
                    q.append(elements[i])

        # print(answerCount)
        # print(visited)

        if answerCount >= numCourses:
            return True
        return False












        
        # if len(prerequisites) < numCourses:
        #     return False
        # if len(prerequisites) == 0:
        #     return True
        # if len(prerequisites) == 1:
        #     return True
        # # tempp = 2 * len(prerequisites)
        # # print(tempp)
        # # if tempp < numCourses:
        # #     return False

    
        # from collections import defaultdict
        # hm = defaultdict(list)

        # maxx = 0
        # for i in range ( 0 , len(prerequisites)):
        #     hm[prerequisites[i][0]].append(prerequisites[i][1])
        #     hm[prerequisites[i][1]].append(prerequisites[i][0])
        #     maxx = max(maxx,prerequisites[i][0],prerequisites[i][1] )

        # # print(hm)
        # visited = [0] * (maxx + 1)
        # ans = True
        # # print(visited)
        # found = -1
        # def bfs (element,parent, visited ):
        #     nonlocal found
        #     if found == 1:
        #         return False
        #     if visited[element] == 1 and element != parent:
        #         return False

        #     visited[element] = 1
        #     temp = hm[element]
        #     for i in range(0 , len(temp)):
        #         answer = True
        #         if element == temp[i]:
        #             answer = False
        #         if temp[i] != parent and answer == True:
        #             answer = bfs(temp[i], element, visited)
        #         if answer == False:
        #             found == 1
        #             return False

        #     return True

        # i = 0
        # while (ans == True and i < len(visited)):
        #     if visited[i] == 0:
        #         if len(hm[i]) > 0:
        #             ans =  bfs(i , -1, visited)
        #     i+=1

        # return ans
                     