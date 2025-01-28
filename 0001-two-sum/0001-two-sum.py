class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index in range(0, len(nums)):
            compliment = target - nums[index]
            if(numbers.get(compliment) != None):
                return [numbers.get(compliment), index]
            else:
                numbers[nums[index]]=index
        return []