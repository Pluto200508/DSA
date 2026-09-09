class Solution:
    def findCeil(self, arr, x):
        guess = 0
        low = 0
        high = len(arr)-1
        res = -1
        c = 0
        while(low <= high):
            guess = (low + high)//2
            
                
            if arr[guess] < x:
                low = guess+1
            if arr[guess] >= x:
                high = guess -1
                res =  guess
           
        
        return res
        