"""
27 - Remove Element
https://leetcode.com/problems/remove-element/


note: When deleting elements of an array while looping with a for, Make an error "Out range of index"
      because total length will be change for every loop.

Tip : I think del command automatically pull one array of list 

Sol : The first element is checked by the length of the list. 
      If nums[0] is different from val, it should remain in the list, 
      so we add it to the end of the list. And remove nums[0]. 
      If nums[0] is equal to val, just remove it.

Summary : It checks the first element as much as the length of the list,
          and if it is val, it is removed, otherwise it is sent back.
"""
class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[0] != val:
                nums.append(nums[0])
                del nums[0]
            else:
                del nums[0]
        
        return len(nums)

