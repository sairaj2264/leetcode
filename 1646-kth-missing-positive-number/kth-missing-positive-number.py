class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        low = 0
        high = len(arr) - 1

        if (arr[0] - 1) == k:
            return (arr[0] - 1)
        
        elif (arr[0] - 1) > k:
            return k

        while (low <= high):
            mid = (low + high)//2

            if (arr[mid] - mid - 1) < k:
                low = mid + 1

            else:
                high = mid - 1

        answer = high + 1 + k 
        return answer
    