class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i != len(s)-1:
                    if s[i+1] == 'V':
                        total += 4
                        i += 1
                    elif s[i+1] == 'X':
                        total += 9
                        i += 1
                    else:
                        total += lookup[s[i]]
                else:
                    total += lookup[s[i]]
            elif s[i] == 'X':
                if i != len(s)-1:
                    if s[i+1] == 'L':
                        total += 40
                        i += 1
                    elif s[i+1] == 'C':
                        total += 90
                        i += 1
                    else:
                        total += lookup[s[i]]
                else:
                    total += lookup[s[i]]
            elif s[i] == 'C':
                if i != len(s)-1:
                    if s[i+1] == 'D':
                        total += 400
                        i += 1
                    elif s[i+1] == 'M':
                        total += 900
                        i += 1
                    else:
                        total += lookup[s[i]]
                else:
                    total += lookup[s[i]]
            else:
                total += lookup[s[i]]
            i += 1
        return total
