class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_ = nums[0]
        for i in range(1,len(nums)):
            if cur <= 0:
                cur = nums[i]
            else:
                cur += nums[i]
            max_ = max(max_,cur)
        return max_