class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        reach = length-1
        for i in range(length-2,-1,-1):
            if nums[i] + i >= reach:
                reach = i
        return reach == 0