class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7

        # Count how many times each value appears
        freq = Counter(arr)

        ans = 0

        # x <= y <= z avoids counting the same triplet multiple times
        for x in range(101):
            if x not in freq:
                continue

            for y in range(x, 101):
                if y not in freq:
                    continue

                z = target - x - y

                # z must be at least y to maintain x <= y <= z
                if z < y or z > 100:
                    continue

                if z not in freq:
                    continue

                # Case 1: x == y == z
                if x == y == z:
                    n = freq[x]
                    ans += n * (n - 1) * (n - 2) // 6

                # Case 2: x == y != z
                elif x == y:
                    ans += (freq[x] * (freq[x] - 1) // 2) * freq[z]

                # Case 3: x != y == z
                elif y == z:
                    ans += freq[x] * (freq[y] * (freq[y] - 1) // 2)

                # Case 4: x, y, z are all different
                else:
                    ans += freq[x] * freq[y] * freq[z]

        return ans % MOD