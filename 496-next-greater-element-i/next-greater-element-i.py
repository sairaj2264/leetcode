class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        hm = {}
        for i in range ( len(nums2) - 1 , -1 , -1):

            if not stack:
                hm[nums2[i]] = -1
                stack.append(nums2[i])
            
            else:
                while (len(stack) > 0):
                    temp = stack[-1]
                    if nums2[i] > temp:
                        stack.pop()
                    else:
                        hm[nums2[i]] = temp
                        stack.append(nums2[i])
                        break

                if len(stack) == 0:
                    stack.append(nums2[i])
                    hm[nums2[i]] = -1
            
        answer = []
        for i in range (0, len(nums1)):
            temp = hm[nums1[i]]
            answer.append(temp)
        
        return answer
            

        
        