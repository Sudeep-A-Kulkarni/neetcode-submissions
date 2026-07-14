class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        memo = {}  # (i, m) -> min_largest_sum

        def dfs(i, m):
            # Base cases
            if i == n and m == 0:
                return 0
            if i == n or m == 0:
                return float("inf")
            if (i, m) in memo:
                return memo[(i, m)]

            res = float("inf")
            cur_sum = 0
            
            # Try splitting the array at every possible index j
            for j in range(i, n - m + 1):
                cur_sum += nums[j]
                
                # Pruning: If cur_sum is already worse than res, further splits won't help
                if cur_sum >= res:
                    break
                
                max_sum = max(cur_sum, dfs(j + 1, m - 1))
                res = min(res, max_sum)

            memo[(i, m)] = res
            return res

        return dfs(0, k)