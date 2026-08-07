class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:



        from collections import deque
        q = deque()
        import heapq
        heap = []
        hm = {}

        for i in range(0 , len(tasks)):
            hm[tasks[i]] = hm.get(tasks[i], 0) + 1

        for keys in hm:
            element = hm[keys]
            heapq.heappush(heap, - element)

        # print(heap)

        time = 0

        while(len(heap) > 0 or len(q) > 0):
            print(heap)
            if len(q) > 0:
                q_element = q[0]
                if q_element[1] == time:
                    heapq.heappush(heap, - q_element[0])
                    temp = q.popleft()
            if len(heap) > 0:
                element = - heapq.heappop(heap)
                time += 1
                element -= 1
                if element > 0:
                    q.append((element, time + n))
            else:
                time += 1

        return time



        # import heapq
        # heap = []
        # # m = len(tasks)
        # # for i in range(0 , m):
        # #     heapq.heappush(heap, tasks[i])

        # hm = {}

        # for task in tasks:
        #     hm[task] = hm.get(task, 0) + 1

        # # Step 2: Get frequencies
        # freq = list(hm.values())

        # # Step 3: Sort descending
        # freq.sort(reverse=True)

        # # Step 4: Build your "heap"
        # heap = []

        # for i in range(len(freq)):
        #     ch = chr(ord('A') + i)

        #     for _ in range(freq[i]):
        #         heap.append(ch)

        # placed = [0]*20
        # counter = 0
        # previous = 0
        # idx = 0
        # hm = {}
        # while (len(heap) > 0):
        #     # print(placed)
        #     element = heapq.heappop(heap)
            
        #     if element == previous:
        #             temp = hm.get(element, -1)
        #             # print(temp)
        #             if temp == -1:
        #                 temp = idx
        #             flag = False
        #             k = 0
        #             while(flag == False):
        #                 if k > n:
        #                     if placed[temp] != 1:
        #                         placed[temp] = 1
        #                         # hm[element] = hm.get(element, 0)
        #                         hm[element] = temp
        #                         previous = element
        #                         flag = True
        #                     else:
        #                         temp += 1
        #                 else:
        #                     temp += 1
        #                     k+=1


        #     elif element != previous:
        #         temp = hm.get(element, -1)
        #         if temp == -1:
        #             while(placed[idx] == 1):
        #                 idx += 1
        #             placed[idx] = 1
        #             hm[element] = idx
        #             idx += 1
        #             previous = element
                
        #         else:
        #             flag = False
        #             k = 0
        #             while(flag == False):
        #                 if k > n:
        #                     if placed[temp] != 1:
        #                         placed[temp] = 1
        #                         # hm[element] = hm.get(element, 0)
        #                         hm[element] = temp
        #                         previous = element
        #                         flag = True
        #                     else:
        #                         temp += 1
                
        #                 else:
        #                     temp += 1
        #                     k+=1
        #     print(placed, element)
                
        #         # placed[idx] = 1
        #         # hm[element] = hm.get(element, 0) + idx
        #         # idx += 1
        # index = 0
        # for i in range(0 , len(placed)):
        #     if placed[i] == 1:
        #         index = i

        # return (index + 1)


        