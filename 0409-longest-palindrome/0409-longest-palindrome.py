class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm={}
        res=0
        odd = False
        for ch in s:
            if ch in hm:
                hm[ch]+=1
            else :
                hm[ch]=1

        for key, value in hm.items():
            if value % 2==0:
                res+=value
            else :
                res+=value-1
                odd = True

        if odd == True:
            return res+1
        else :
            return res