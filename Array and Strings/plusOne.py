class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        new_digits = []
        for num in digits[::-1]:
            x = (num + carry) % 10
            carry = int((num + carry) / 10)
            new_digits.append(x)
        if carry != 0:
            new_digits.append(carry)
        return new_digits[::-1]




