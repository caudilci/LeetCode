class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        i, j, carry = 0, 0, 0
        result = []
        while i < len(a) or j < len(b):
            current = 0
            if i >= len(a):
                current = int(b[j]) + carry
            elif j >= len(b):
                current = int(a[i]) + carry
            else:
                current = int(a[i]) + int(b[j]) + carry
            carry = 0
            if current > 1:
                carry = 1
                current -= 2
            result.append(current) 
            i += 1
            j += 1
        while carry > 0:
            carry -= 1
            result.append(1)
        result.reverse()
        return "".join(map(str, result))

        