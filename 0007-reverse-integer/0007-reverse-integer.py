class Solution:
    def reverse(self, x: int) -> int:
        isPositive = x >= 0
        digits = len(x.__str__())- 1
        digits = digits - 1 if not isPositive else digits
        resultlist = []
        result = 0
        d = 0
        x = x if isPositive else x * -1
        while digits >= 0:
            current = math.floor(x / 10 ** digits)
            x -= current * 10**digits
            result += current * 10 ** d
            digits -= 1
            d += 1
        result = result if isPositive else result * -1
        return result if result <= 2**31 - 1 and result >= -2**31 else 0