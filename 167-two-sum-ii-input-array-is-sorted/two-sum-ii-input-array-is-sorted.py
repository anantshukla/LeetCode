class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            tSum = numbers[l] + numbers[r]
            if tSum == target:
                return (l + 1, r + 1)
            elif tSum > target:
                r -= 1
            else:
                l += 1
        