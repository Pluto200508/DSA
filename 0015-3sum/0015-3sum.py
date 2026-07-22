class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                current_sum = nums[l] + nums[r]

                if current_sum == target:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif current_sum < target:
                    l += 1

                else:
                    r -= 1

        return ans