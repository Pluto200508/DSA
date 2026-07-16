class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0
        n = x
        while(x>0):
            d=x%10
            r=r*10+d
            x=x//10
        if n == r:
            return True
        else :
            return False
    