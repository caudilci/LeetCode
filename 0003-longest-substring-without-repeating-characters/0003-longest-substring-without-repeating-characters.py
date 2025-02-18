class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        current = ""
        longest = 0
        last_start = 0
        while end != len(s):
            if current.find(s[end]) == -1:
                current = current + s[end]
            else:
                last_start = start
                start = current.find(s[end])+1 + last_start
                current = s[start:end+1]
            longest = len(current) if len(current) > longest else longest
            end += 1
        return longest