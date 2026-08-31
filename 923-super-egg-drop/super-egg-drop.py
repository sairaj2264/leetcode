class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        dp = {}
        def recurse(e, f):
            if f == 0 or f == 1:
                return f

            if e == 1:
                return f
            if (e, f) in dp:
                return dp[(e, f)]
            low = 1
            high = f
            minn = float('inf')

            while low <= high:

                floor = (low + high) // 2

                broken = recurse(e - 1, floor - 1)
                not_broken = recurse(e, f - floor)

                temp = 1 + max(broken, not_broken)
                minn = min(minn, temp)
                if broken < not_broken:
                    low = floor + 1
                else:
                    high = floor - 1

            dp[(e, f)] = minn
            return minn
        
        answer = recurse(k,n)
        return answer