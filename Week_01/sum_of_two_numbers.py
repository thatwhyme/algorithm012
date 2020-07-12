def find(nums:List[int],a:int,b:int) -> List[int]:
        i = 0
        flag1 = True
        flag2 = True
        length =len(nums)
        while(i< length and flag1):
            if nums[i] == a:
                s = i
                flag1 =False
            i += 1
        i = 0
        
        while(i<length  and flag2):
            if nums[i] == b:
                t = i
                if a==b:
                    i += 1
                    continue
                else: 
                    flag2 =False 
            i += 1
        return s,t
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        co = list(nums)
        nums.sort()
        i = 0
        j = len(nums) -1
        while i<j:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
                while(i< j and nums[i] == nums[i-1]):
                    i += 1
            elif sum >target:
                j -= 1
                while(i<j and nums[j] == nums[j+1]):
                    j -= 1
            else:
                return find(co,nums[i],nums[j])