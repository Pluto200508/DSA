class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def solve(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if s1 == s2:
                return True

            if sorted(s1) != sorted(s2):
                return False

            n = len(s1)

            for i in range(1, n):
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True

                if solve(s1[:i], s2[n-i:]) and solve(s1[i:], s2[:n-i]):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return solve(s1, s2)