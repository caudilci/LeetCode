class Solution:
    letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
    }
    def solve(self, index: int, digits: str, answer: List[str], temp: str):
        if index == len(digits):
            answer.append(temp)
            return
        
        for character in self.letters[digits[index]]:
            self.solve(index + 1, digits, answer, temp + character)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        answer = []
        self.solve(0, digits, answer, "")
        return answer