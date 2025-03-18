class Solution:
    def findComplement(self, num: int) -> int:
        binLen = len(bin(num))-2
        one = "1"
        mask = f"{one*binLen}"
        return int(mask, 2) ^ num