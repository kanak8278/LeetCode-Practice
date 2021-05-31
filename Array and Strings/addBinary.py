class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def utilAdd(a, b, carry):
            if int(a) + int(b) + carry == 3:
                print(3)
                val = 1
                carry = 1
            elif int(a) + int(b) + carry == 2:
                print(2)
                val = 0
                carry = 1
            elif int(a) + int(b) + carry == 1:
                print(1)
                val = 1
                carry = 0
            else:
                print(0)
                val = 0
                carry = 0
            print(val, carry)
            return val, carry

        carry = 0
        rev_a = a[::-1]
        rev_b = b[::-1]
        sum_rev = str()

        for idx in range(max(len(rev_a), len(rev_b))):
            if idx < len(rev_a) and idx < len(rev_b):
                print(idx, rev_a[idx], rev_b[idx], carry)
                val, carry = utilAdd(rev_a[idx], rev_b[idx], carry)
            if idx < len(rev_a) and idx >= len(rev_b):
                print(idx, rev_a[idx], 0, carry)
                val, carry = utilAdd(rev_a[idx], "0", carry)
            if idx >= len(rev_a) and idx < len(rev_b):
                print(idx, 0, rev_b[idx], carry)
                val, carry = utilAdd("0", rev_b[idx], carry)
            sum_rev += str(val)

        if carry != 0:
            sum_rev += str(carry)
        return sum_rev[::-1]
        # for s in sum_rev[::-1]:




