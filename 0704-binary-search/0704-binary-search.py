class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        guess = 0
        while (low<=high):
            guess = (low + high)//2
            if nums[guess] == target :
                return guess
            if nums[guess] < target :
                low = guess + 1
            if nums[guess] > target :
                high = guess - 1
        return -1

