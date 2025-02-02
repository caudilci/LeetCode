from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        neg, pos = defaultdict(int), defaultdict(int)
        zero = 0
        for num in nums:
            if num < 0:
                neg[num] += 1
            elif num > 0:
                pos[num] += 1
            else:
                zero += 1
        if zero:
            for num in pos:
                if -1*num in neg:
                    result.add((-1*num, 0, num))
            if zero >= 3:
                result.add((0,0,0))
        for asc, desc in ((neg, pos), (pos, neg)):
            asc_items = list(asc.items())
            for index, (neg_item, pos_item) in enumerate(asc_items):
                for neg_item2, pos_item2 in asc_items[index:]:
                    if neg_item != neg_item2 or (neg_item == neg_item2 and pos_item > 1):
                        if -neg_item-neg_item2 in desc:
                            result.add((neg_item, neg_item2, -neg_item-neg_item2))       
        return list(result)