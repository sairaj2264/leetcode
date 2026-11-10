class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        

        count = 0

        def count_pairs(nums, low, mid, high):
            nonlocal count
            l1 = low
            r1 = mid
            l2 = mid + 1
            r2 = high
            temp = []

            while (l1 <= r1 and l2 <= r2):
                if nums[l1] > 2*nums[l2]:
                    count += (r1 - l1 +1)
                    l2 += 1
                else:
                    l1 += 1

        def merge(nums, low, mid, high):
            l1 = low
            r1 = mid

            l2 = mid + 1
            r2 = high
            temp = []

            count_pairs(nums, low, mid, high)

            while (l1 <= r1 and l2 <= r2):
                if (nums[l1] <= nums[l2]):
                    temp.append(nums[l1])
                    l1 += 1
                else:
                    temp.append(nums[l2])
                    l2 += 1
            
            while (l1 <= r1):
                temp.append(nums[l1])
                l1 += 1

            while (l2 <= r2):
                temp.append(nums[l2])
                l2 += 1

            idx = 0
            for i in range(low, high + 1):
                nums[i] = temp[idx]
                idx += 1




            

        
        def merge_sort(nums, low, high):
            if low < high:
                mid = (low + high)//2
                merge_sort(nums, low, mid)
                merge_sort(nums, mid + 1, high)
                merge(nums, low, mid, high)

        merge_sort(nums, 0 , (len(nums) -1))
        return count

        