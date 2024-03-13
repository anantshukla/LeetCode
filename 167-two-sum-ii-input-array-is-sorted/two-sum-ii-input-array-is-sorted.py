class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        tSum = numbers[l] + numbers[r]
        while tSum != target:
            if tSum > target:
                r -= 1
            else:
                l += 1
            tSum = numbers[l] + numbers[r]
        return (l + 1, r + 1)

        # n = len(numbers)
        # l, r = 0, n - 1
        # while l < r:
        #     tSum = numbers[l] + numbers[r]
        #     if tSum == target:
        #         return (l + 1, r + 1)
        #     elif tSum > target:
        #         r -= 1
        #     else:
        #         l += 1
        