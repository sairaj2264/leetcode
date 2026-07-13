class Solution:
    def jump(self, nums: List[int]) -> int:
        arr = nums.copy()

        arr[-1] = 0
        for i in range (len(arr) -2, -1, -1):
            if arr[i] == 0:
                continue
            temp = arr[i]

            if i + temp >= len(arr) - 1:
                arr[i] = 1
                continue

            temp2 = 100000

            while (temp > 0):
                if arr[i + temp] == 0 and (i+temp) < (len(arr) -1):
                    temp -=1
                    continue
                temp2 = min(temp2, arr[i + temp])
                temp -= 1

            arr[i] = temp2 + 1
            # print(temp, temp2)


        return arr[0]

            
        