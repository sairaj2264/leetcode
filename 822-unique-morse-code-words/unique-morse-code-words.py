class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        answer = []
        for word in words:
            temp = []
            for letter in word:
                index = ord(letter) - ord('a')
                temp.append(alpha[index])
            temp = "".join(temp)
            if temp not in answer:
                answer.append(temp)

        return len(answer)
