class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm1 = {}

        for ch in text:
            if ch in hm1:
                hm1[ch] += 1
            else:
                hm1[ch] = 1

        hm2 = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        ans = float('inf')

        for k in hm2:
            available = hm1.get(k, 0)
            required = hm2[k]

            possible = available // required
            ans = min(ans, possible)

        return ans