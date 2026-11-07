class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        self.sum = 0
        for i in range(self.left, self.right +1):
            self.sum += self.nums[i]

        return self.sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)