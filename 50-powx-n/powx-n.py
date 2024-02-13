class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recPow(b, p):
            if b == 0: return 0
            if p == 0: return 1
            
            res = recPow(b * b, p//2)
            # res = res * res
            return res * b if p%2 else res

        ans = recPow(x, abs(n))
        return 1/ans if(n < 0) else ans

        