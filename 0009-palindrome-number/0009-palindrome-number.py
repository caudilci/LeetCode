class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = x.__str__()
        index = 0
        jndex = len(xstr)-1
        while index <= jndex and jndex >= index:
            if xstr[index] != xstr[jndex]:
                return False
            else:
                index += 1
                jndex -= 1
        return True