class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        cookies = s
        children = g

        # print(cookies)
        cookies.sort()
        children.sort()

        answer = 0
        i = 0
        j = 0
        while (i < len(cookies) and j < len(children)):
            print(cookies[i], children[j])
            if cookies[i] >= children[j]:
                i+=1
                j+=1
                answer +=1

            else:
                i+=1
    
        return answer