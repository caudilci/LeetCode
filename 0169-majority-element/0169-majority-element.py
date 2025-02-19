class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = {}
        most = None
        for num in nums:
            if occurences.get(num):
                if occurences[num] > len(nums) / 2:
                    return num
                occurences[num] += 1
                if not most:
                    most = num
                elif occurences[most] < occurences[num]:
                    most = num
            else:
                occurences[num] = 1
                if not most:
                    most = num
                elif occurences[most] < occurences[num]:
                    most = num
        return most