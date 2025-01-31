class Solution:
    def isValid(self, s: str) -> bool:
        counts = {
            '(': 0,
            ')': 0,
            '[': 0,
            ']': 0,
            '{': 0,
            '}': 0,
        }
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        last_opening = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                last_opening.append(c)
            if c == ')' or c == ']' or c == '}':
                if len(last_opening) == 0 or c != pairs[last_opening[len(last_opening) - 1]]:
                    return False
                else:
                    last_opening.pop()
            counts[c] += 1
        return counts['('] == counts[')'] and counts['['] == counts[']'] and counts['{'] == counts['}']