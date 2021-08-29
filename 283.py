"""
283 - Move Zeros

Note: Swap two values in the Python 
        a = 3             =>     a = "abc"
        b = "abc"         =>     b = 3

        a , b = b , a 
"""
class Solution(object):
    def moveZeroes(self, nums):
        place = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[place], nums[i] = nums[i], nums[place]
                place += 1

