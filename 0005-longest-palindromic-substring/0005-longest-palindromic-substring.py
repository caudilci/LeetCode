class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        middle = 0
        current = ""
        longest = ""
        while middle < len(s):
            if start < 0 or end >= len(s):
                longest = current if len(current) > len(longest) else longest
                current = ""
                middle += 0.5
                start = math.floor(middle)
                end = math.ceil(middle)
            elif s[start] == s[end]:
                current = s[start:end+1]
                start -= 1
                end += 1
            else:
                longest = current if len(current) > len(longest) else longest
                current = ""
                middle += 0.5
                start = math.floor(middle)
                end = math.ceil(middle)
        return longest
