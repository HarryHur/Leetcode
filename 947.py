"""
947 - Valid Mountain Array

Sol: I used peak
    1. Set two poiner p1 = 0, p2 = len(arr) - 1
    2. peak = max(arr) 
    3. peakplace = arr.index(peak)
    We have 3 cases
    Case 1 - Peak cannot be in first or last  -> That is not valid mountain ex) 321, 234
    Case 2 - Need to check increases is correct 
            During p1 < peakplace : 
                if arr[p1] >= arr[p1+1] => false
                p1++
    Case 3 - Need to check decrease is correct
            During p2 > peakplace:                       
                if arr[p2] >= arr[p2-1] => false   ex) 3 1 2 0   p2 = 2 p2 - 1 = 1 
                p2-- 
"""
class Solution(object):
    def validMountainArray(self, arr):
        p1 = 0
        p2 = len(arr) - 1
        peak = max(arr)
        peakPlace = arr.index(peak)
        
        if peakPlace == p1 or peakPlace == p2 :
            return False
        
        while p1 < peakPlace :
            if arr[p1] >= arr[p1 + 1]:
                return False
            p1 += 1
            
        while p2 > peakPlace :
            if arr[p2] >= arr[p2 - 1]:
                return False
            p2 -= 1
            
        
        return True