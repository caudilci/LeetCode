class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = []
        stringlist = []
        for i in range(0, numRows):
            lists.append([])
        index = 0
        i = 0
        ascending = True
        while index < len(s):
            if i >= numRows:
                i = numRows - 2 if numRows > 1 else 0
                ascending = False
            if i < 0:
                i = 1 if numRows > 1 else 0
                ascending = True
            lists[i].append(s[index])
            i = i + 1 if ascending else i - 1
            index += 1 
        for i in range(0, numRows):
            stringlist.append("".join(lists[i]))
        return "".join(stringlist)