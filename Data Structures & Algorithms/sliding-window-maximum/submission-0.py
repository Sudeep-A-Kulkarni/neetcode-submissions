from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Stores indices of elements
        res = []
        
        for i in range(len(nums)):
            # 1. Maintain monotonic decreasing property
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            # 2. Append current element's index
            q.append(i)
            
            # 3. Remove index if it falls out of the left bound of the window
            if q[0] < i - k + 1:
                q.popleft()
                
            # 4. Append maximum element to results once window hits size k
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
