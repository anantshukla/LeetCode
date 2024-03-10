class Solution:
    def isHappy(self, n: int) -> bool:  
        def getDigits(num):
            squares = 0
            while num != 0:
                squares += (num % 10) ** 2
                num //= 10
            return squares

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getDigits(n)
        return n == 1
