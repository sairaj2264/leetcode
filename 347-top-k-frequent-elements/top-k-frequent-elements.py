class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listt = defaultdict(lambda: 0)

        for num in nums:
            valuee = listt[num]
            listt[num] = valuee+1

            ans = []

        listt = sorted(listt, key=listt.get, reverse=True)

        for i in range (0,k):
            ans.append(listt[i])

        return ans

        