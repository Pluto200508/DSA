class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            su = -1*nums[i]
            while(left < right):
                
                if su == nums[left] + nums[right]:
                    
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left<n and nums[left] == nums[left-1] :
                        left+=1
                elif su < nums[left] + nums[right]:
                    right-=1
                    while right > 0 and nums[right] == nums[right + 1]:
                        right-=1
                else:
                    left +=1
        return res



        