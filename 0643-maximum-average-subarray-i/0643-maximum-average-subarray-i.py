class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = 0
        high = k
        n = len(nums)

        su = sum(nums[low:high])
        max_avg = su / k

        while high < n:
            su = su - nums[low] + nums[high]
            low += 1
            high += 1

            avg = su / k
            if avg > max_avg:
                max_avg = avg

        return max_avg