class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        answer = []
        temp = ""
        def digitPicker(counter,digits, answer, temp):
            if len(temp) == len(digits):
                answer.append(temp)
                return

            for c in mapping[digits[counter]]:
                digitPicker(counter + 1, digits, answer, temp + c)
                
        if not digits:
            return []
        digitPicker(0, digits, answer, temp)
        return answer

