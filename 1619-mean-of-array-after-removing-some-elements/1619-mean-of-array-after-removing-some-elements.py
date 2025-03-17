class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sortedArr = sorted(arr)
        start,end = round(len(arr) * 0.05), len(arr) - round(len(arr) * 0.05)
        count = end - start
        total = 0
        for i in range(start, end):
            total += sortedArr[i]
        return total/count