class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        answer = 0

        for j in range(n - 1):
            freq = [0] * 27

            seen = set()

            for i in range(j, -1, -1):
                seen.add(s[i])
                freq[len(seen)] += 1


            seen = set()

            for k in range(j + 1, n):
                seen.add(s[k])
                answer += freq[len(seen)]

        return answer