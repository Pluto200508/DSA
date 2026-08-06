class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = float('inf')
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while(left<right):
                su = nums[i]+nums[left]+nums[right]
                diff = abs(su-target)
                if max_diff > diff :
                    max_diff = diff
                    res= su
                if su > target :
                    right -=1
                if su < target :
                    left +=1
                if su == target :
                    res = su
                    break
        return res