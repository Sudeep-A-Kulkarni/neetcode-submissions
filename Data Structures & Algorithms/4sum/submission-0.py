class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_list = []
        lst1 = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if (nums[i]+nums[j]+nums[k]+nums[l] == target):
                            lst1 = [nums[i], nums[j], nums[k], nums[l]]
                            lst1.sort()
                            if lst1 not in ans_list:  # Also stops some duplicates, though slow
                                ans_list.append(lst1)

        return ans_list

