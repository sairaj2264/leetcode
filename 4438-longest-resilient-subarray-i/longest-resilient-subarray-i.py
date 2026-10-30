class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        from collections import deque
        q = deque()
        arr = [-1] * len(nums)
        prev = None
        count = 0
        for i in range(0 , len(nums)):
            current = nums[i]%k
            if prev is None:
                prev = current
                arr[i] = count
            elif prev == current:
                arr[i] = count
            else:
                count += 1
                prev = current
                arr[i] = count
        prev = 0
        # print(arr)
        first = 0
        last = 0
        sums = []
        summ = 0
        for i in range(0 , len(nums)):
            if i == 0:
                prev = arr[i]
            current = arr[i]
            if current == prev:
                summ += nums[i]
            else:
                sums.append(summ)
                summ = nums[i]
                prev = current
        if summ > 0:
            sums.append(summ)
        # print(sums)
        i = 0
        left= 0
        prev = 0
        ranges = []
        r = 0
        for j in range(0 , len(arr)):
            current = arr[j]
            summ = 0
            if j == 0:
                prev = current
            if current == prev:
                summ = sums[i]
            else:
                ranges.append((left,j-1, nums[left]%k) )
                left = j
                i += 1
                summ = sums[i]
                prev = current

            arr[j] = summ - nums[j]
        if left < len(arr):
            ranges.append((left, (len(arr) - 1), nums[left]%k))
        # print(arr)
        # print(sums)
        # print(ranges)
        answer = 1

        i = 0

        for i,j,r in ranges:

            length = j - i + 1
            p = k // gcd(r, k)

  
            count = length - (length - 1) % p
            # count = 0
            # for l in range(i, (j +1)):
            #     if arr[l]%k == 0:
            #         count += 1
            answer = max(count, answer)
            #     else:
            #         count = 0
        return answer


             