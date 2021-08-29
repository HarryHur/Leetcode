"""
28 - Remove Duplicates from Sorted Array  Solution 
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Sol : If nums[i] and nums[i+1] are different while iterating through the loop, 
    it means that the duplicate value is over, so nums[index] = nums[i+1] is a new value.
    After the loop is finished, duplicates are removed as much as the index length of the nums array.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        
        index = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                index += 1
                nums[index] = nums[i+1]
                
                
        return index+1
            