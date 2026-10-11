class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        words = set()
        if endWord not in wordList:
            return 0
        
        
        q = deque()
        q.append(beginWord)

        for word in wordList:
            words.add(word)
        
        if beginWord in words and wordList:
            words.remove(beginWord)
        def convert(arr,j):
            i = 0
            ans = []
            while i < len(arr):
                temp = chr(arr[i])
                ans.append(temp)
                i += 1
            final_ans = ''.join(ans)
            return final_ans


        def compute(word):
            i = 0
            arr = []
            brr = []
            while i < len(word):
                arr.append(ord(word[i]))
                brr.append(ord(word[i]))
                i += 1
            for i in range (0 , len(arr)):
                arr = brr.copy()
                memory = arr[i]
                for j in range(0 , 26):
                    if ord('a') + j == memory:
                        continue
                    arr[i] = ord('a') + j
                    final_word = convert(arr,j)
                    
                    if final_word in words:
                        q.append(final_word)
                        words.remove(final_word)

            
        count = 0
        while len(q) > 0:
            q_length = len(q)
            pops = 0
            count += 1
            while pops < q_length:
                word = q.popleft()
                if word == endWord:
                    return count
                pops += 1
                compute(word)

        if endWord in words:
            return 0
        return count
        











        # from collections import deque, defaultdict
        # adj = defaultdict(list)
        # q = deque()
        # in_degree = {}
        # charecters = set()
        # if endWord not in wordList:
        #     return 0
        # for i in range(0 , len(wordList) - 1):
        #     words1 = wordList[i]
        #     words2 = wordList[i+1]

        #     j = 0
        #     while (j < len(words1) and j < len(words2) and words1[j] == words2[j]):
        #         charecters.add(words1[j])
        #         charecters.add(words2[j])
        #         j += 1
        #     if j > len(words1) or j > len(words2):
        #         continue
            
        #     charecters.add(words1[j])
        #     charecters.add(words2[j])
        #     adj[words1[j]].append(words2[j])
        #     in_degree[words2[j]] = in_degree.get(words2[j],0) + 1


        # for values in charecters:
        #     if values not in in_degree.keys():
        #         q.append(values)

        # sorted_nodes = []
        # number_of_operations = 0
        # while len(q) > 0:
        #     element = q.popleft()
        #     sorted_nodes.append(element)
        #     elements = adj[element]
        #     number_of_operations += 1
        #     for node in elements:
        #         in_degree[node] -= 1
        #         if in_degree[node] == 0:
        #             q.append(node)
        
        # if number_of_operations < len(charecters):
        #     return 0


        # i = 0
        # while (beginWord[i] == endWord[i]):
        #     i += 1

        # ans = 0
        # start = 0
        # end = 0
        # for j in range(0,len(sorted_nodes)):
        #     if sorted_nodes[j] == beginWord[i]:
        #         start = j
        #     if sorted_nodes[j] == endWord[i]:
        #         end = j

        # ans = (end - start) - 1
        # return ans


        

