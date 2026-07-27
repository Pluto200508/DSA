class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range (len(haystack)-len(needle)+1):
            match = True 
            for j in range(len(needle)):

                if haystack[i+j] != needle[j]:
                    match = False
            if match :
                return i
            else :
                continue 
        return -1

