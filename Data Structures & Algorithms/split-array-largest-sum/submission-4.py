
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Cache the results of dfs(i, m) to prevent redundant calculations
        @lru_cache(None)
        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else float("inf")
            if m == 0:
                return float("inf")

            res = float("inf")
            curSum = 0
            # n - m + 1 ensures we leave at least (m - 1) elements for the remaining splits
            for j in range(i, n - m + 1):
                curSum += nums[j]
                
                # If the current sum already exceeds our best result, 
                # we can optimize by breaking early (since elements are non-negative)
                if curSum >= res:
                    break
                    
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            return res

        return dfs(0, k)