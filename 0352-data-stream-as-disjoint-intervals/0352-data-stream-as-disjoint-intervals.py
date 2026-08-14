class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        nums = sorted(self.nums)
        ans = []

        if not nums:
            return ans

        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ans.append([start, end])
                start = nums[i]
                end = nums[i]

        ans.append([start, end])

        return ans