class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        digit = 3
        result = ""
        while digit >= 0:
            amount = math.floor(num/(10**digit))
            num -= amount * (10 ** digit)
            if amount == 4 or amount == 9:
                result += lookup[amount * (10 ** digit)]
            else:
                if amount >= 5:
                    result += lookup[5 * 10 ** digit]
                    amount -= 5
                while amount > 0:
                    result += lookup[10 ** digit]
                    amount -= 1
            digit -= 1
        return result