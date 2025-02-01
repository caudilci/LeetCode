class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        downshift = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                downshift += 1
            elif downshift != 0:
                nums[i-downshift]=nums[i]
        return len(nums) - downshift