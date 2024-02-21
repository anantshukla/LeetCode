class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans, ctr = None, 0
        for i in range(1, n + 1):
            if n % i == 0:
                ctr += 1
                if ctr == k:
                    ans = i
        return ans if ctr >= k else -1
        