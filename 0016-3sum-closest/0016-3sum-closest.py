class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        diff = float('inf')
        n = len(nums)
        for i in range (n-2):
            l = i+1
            r = n-1
            while (l<r):

                total = nums[i]+nums[r]+nums[l]
                d = abs(total-target)
                if diff>d :
                    diff = d
                    res =  total
                if total == target :
                    return res
                if total > target:
                    r-=1
                else :
                    l+=1
        return res 