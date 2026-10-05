class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        arr = nums
        high = len(nums) -  1

        answer = -1
        if len(arr) == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        else:
            low = 1

        if arr[len(nums) - 1] > arr[len(nums) - 2]:
            return len(nums) - 1
        else:
            high = len(nums) - 2


        while (low <= high):
            mid = (low + high)//2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                answer = mid
                break

            if arr[mid] < arr[mid - 1]:
                high = mid - 1

            else:
                low = mid + 1
        return answer

