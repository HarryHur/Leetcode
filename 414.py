"""
414 - Third Maximum Number
"""
class Solution(object):
    def thirdMax(self, nums):
        
        sort = sorted(nums, reverse = True)    
        maxval = sort[0]
        notmaxval = maxval
        result = 0
        
        for i in range(len(sort)):
            if result == 2:
                break
            if sort[i] < maxval:
                maxval = sort[i]
                result += 1
                
        if result < 2:
            return notmaxval
        else:
            return maxval