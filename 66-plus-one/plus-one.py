class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        pos = len(digits) - 1

        while pos >=0:
            digits[pos] += carry
            carry = 0
            if digits[pos] < 10:
                return digits
            carry = digits[pos] // 10
            digits[pos] %= 10
            pos -= 1
        digits.insert(0, carry)
        return digits
