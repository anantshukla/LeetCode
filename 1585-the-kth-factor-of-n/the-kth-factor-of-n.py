class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = []
        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)
        return arr[k - 1] if len(arr) > k-1 else -1
        