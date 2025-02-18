class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j] or (nums1[i] == 0 and i >= m):
                self.insert(nums1, i, nums2[j])
                m += 1
                j += 1
            i += 1
    
    def insert(self, nums: List[int], index: int, value: int):
        prev = nums[index]
        nums[index] = value
        for i in range(index + 1, len(nums)):
            current = prev
            prev = nums[i]
            nums[i] = current