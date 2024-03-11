class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

        # # TC: O(32) = O(1): m = n AND 1. If m == n, last bit had a 1, then right bit-shift (or divide by 2)
        # count = 0
        # while n:
        #     if n & 1:
        #         count += 1
        #     n >>= 1
        # return count
