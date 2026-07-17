class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = 0
        j = 0
        merged = []
        while (i < len(nums1) and j < len(nums2)):

            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        
        while(i < len(nums1)):
            merged.append(nums1[i])
            i+=1

        while (j < len(nums2)):
            merged.append(nums2[j])
            j+=1
        

        temp = len(merged)

        answer = 0
        if temp % 2 == 0:
            temp = int((ceil(len(merged))/2))
            answer = round((merged[temp -1 ] + merged[temp])/2, 5)
        else:
            temp = int((len(merged) - 1)/2)
            answer = merged[temp]

        return answer

        