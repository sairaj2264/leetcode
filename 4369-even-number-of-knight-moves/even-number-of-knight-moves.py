class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:

        diff1 = abs(start[0] - target[0])
        diff2 = abs(start[1] - target[1])

        if (diff1 + diff2) % 2 == 0:
            return True

        else:
            return False
        