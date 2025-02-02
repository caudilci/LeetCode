class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sys.maxsize
        tuples = {}
        for i in range(0, len(nums)):
            low, high = i+1, len(nums)-1
            while low < high:
                temp = nums[i] + nums[low] + nums[high]
                if temp == target:
                    return target
                elif abs(target-temp) < abs(target-closest):
                    closest = temp
                elif temp > target:
                    high -= 1
                else:
                    low += 1
        return closest