class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for num in nums:
            if num>=0:
                a.append(num)
            else :
                b.append(num)
        i = len(a)
        j= len(b)
        if j == 0:
            return [x*x for x in a]
        if i ==0:
            re =[ x*x for x in b]
            re.reverse()
            return re
        a = [x*x for x in a]
        b = [x*x for x in b][::-1]
        re = []
        n = len(a)
        m = len(b)
        i = j = 0
        while i<n and j<m:
            if a[i]<b[j]:
                re.append(a[i])
                i+=1
            else :
                re.append(b[j])
                j+=1
        while i<n :
            re.append(a[i])
            i+=1
        

        while j<m:
            re.append(b[j])
            j+=1
        return re

