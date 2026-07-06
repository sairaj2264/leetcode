class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        stack = deque()
        
        for c in s:
            if len(stack) == 0 and mp[c] > 0:
                stack.append(mp[c])

            elif len(stack) == 0 and mp[c] < 0:
                return False

            elif mp[c] < 0:
                if stack[-1] + mp[c] != 0:
                    return False
                else:
                    stack.pop()
            elif mp[c] > 0:
                stack.append(mp[c])

        if len(stack) == 0:
            return True
        return False
                    
        