class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # wait while we find a non-zero element to
            # switch with you
            # if nums[slow] != 0:
                slow += 1
            # keep going
            fast += 1