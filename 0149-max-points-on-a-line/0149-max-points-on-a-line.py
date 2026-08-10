from typing import List
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        ans = 0

        for i in range(len(points)):
            slopes = {}

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1

            current = max(slopes.values(), default=0) + 1
            ans = max(ans, current)

        return ans