"""
1089 - Duplicates Zero
https://leetcode.com/problems/duplicate-zeros/

"""
class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)
        
        while(i < n):
            if arr[i] == 0: #if arr[i] = 0 , remomve the last value and insert 0 at that place(i) (because we need to duplicate 0)
                arr.pop()
                arr.insert(i, 0)
                i += 1
            i+=1
        