class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recurse(left, right, s):
            # if string length corresponds to the amount of pairs, return
            if len(s) == n * 2:
                res.append(s)
                return
            # if we haven't reached the amount of opening parentheses recurse after adding another opening parentheses
            if left < n:
                recurse(left + 1, right, s + '(')
            # if opening parentheses is more than closing parentheses then recurse with another closing parentheses
            if right < left:
                recurse(left, right + 1, s + ')')
        
        recurse(0, 0, '')
        return res