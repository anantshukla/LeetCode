class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        fProd, rProd = 1, 1
        for i in range(0, n):
            res[i] *= fProd
            fProd *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= rProd
            rProd *= nums[i]
        return res
        
        