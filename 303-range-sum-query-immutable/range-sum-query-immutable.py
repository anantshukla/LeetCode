class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArray = [0] * len(nums)
        if len(nums) > 0:
            self.sumArray[0] = nums[0]
        for i in range(1, len(nums)):
            self.sumArray[i] += self.sumArray[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        lVal = self.sumArray[left - 1] if left > 0 else 0
        rVal = self.sumArray[right]
        return rVal - lVal
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)