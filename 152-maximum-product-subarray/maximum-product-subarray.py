class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        product = 1
        maxx = float('-inf')

        for i in nums:
            product *= i
            maxx = max(product, maxx)
            if product == 0:
                product = 1

        product = 1
        for j in range(n-1,-1,-1):
            product *= nums[j]
            maxx = max(maxx, product)
            if product == 0:
                product = 1

            


        
        return maxx
        