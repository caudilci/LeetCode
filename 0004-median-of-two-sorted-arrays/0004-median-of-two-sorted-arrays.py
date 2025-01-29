class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        isEven = (len(nums1) + len(nums2)) % 2 == 0
        half = math.ceil((len(nums1) + len(nums2))/2)
        half = half + 1 if isEven else half
        i = j = 0
        merged = []
        while len(merged) < half:
            if i < len(nums1):
                if j < len(nums2):
                    if nums1[i] <= nums2[j]:
                        merged.append(nums1[i])
                        i+=1
                    else:
                        merged.append(nums2[j])
                        j+=1
                else:
                    merged.append(nums1[i])
                    i+=1
            elif j < len(nums2):
                merged.append(nums2[j])
                j+=1
        print(merged)
        return merged[len(merged)-1] if not isEven else (merged.pop() + merged.pop())/2

