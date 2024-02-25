class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArray = [0] * len(nums)
        tempSum = 0
        for i, val in enumerate(nums):
            tempSum += val
            self.sumArray[i] = tempSum


    def sumRange(self, left: int, right: int) -> int:
        lVal = self.sumArray[left - 1] if left > 0 else 0
        rVal = self.sumArray[right]
        return rVal - lVal
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)