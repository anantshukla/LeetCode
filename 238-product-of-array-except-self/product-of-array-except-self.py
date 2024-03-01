class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodArr = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prodArr[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prodArr[i] *= prod
            prod *= nums[i]
        return prodArr