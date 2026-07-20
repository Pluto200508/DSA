class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm1={}
        hm2 = {}
        for ch in ransomNote:
            if ch in hm1:
                hm1[ch]+=1
            else :
                hm1[ch]=1
        for hc in magazine :
            if hc in hm2:
                hm2[hc]+=1
            else:
                hm2[hc]=1
        for k in hm1:
            if k not in hm2:
                return False
            if hm2[k]<hm1[k]:
                return False
        return True



