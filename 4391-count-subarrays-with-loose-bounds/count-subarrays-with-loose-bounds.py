class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        
        counts = []
        count = 0
        for i in nums:
            if i >= minK and i <= maxK:
                count += 1
            else:
                counts.append(count)
                count = 0

        counts.append(count)

        answer = 0
        for i in counts:
            if i == 0:
                continue
            answer += ((i*(i+1))//2)
        return answer


