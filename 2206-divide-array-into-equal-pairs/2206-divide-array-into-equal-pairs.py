class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if counts.get(num):
                counts[num] += 1
            else:
                counts[num] = 1
        for count in counts.values():
            if count % 2 != 0:
                return False
        return True