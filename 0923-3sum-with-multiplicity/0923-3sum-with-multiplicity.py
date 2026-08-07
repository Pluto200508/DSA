class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        ans = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if s < target:
                    left += 1

                elif s > target:
                    right -= 1

                else:
                    # Case 1: left and right values are different
                    if arr[left] != arr[right]:
                        left_count = 1
                        right_count = 1

                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left_count += 1
                            left += 1

                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right_count += 1
                            right -= 1

                        ans += left_count * right_count
                        left += 1
                        right -= 1

                    # Case 2: all values between left and right are equal
                    else:
                        m = right - left + 1
                        ans += m * (m - 1) // 2
                        break

        return ans % MOD