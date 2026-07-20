class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for ch in s:
            if ch in hm:
                hm[ch]+=1
            else:
                hm[ch]=1
        for i in range (len(s)):
            if hm[s[i]]==1:
                return i
        return -1
