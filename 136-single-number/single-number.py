class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use XOR. The repeated elements will XOR to 0 and the non repeated will stay as it is.
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
        