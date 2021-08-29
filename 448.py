"""
448 - Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        result = []
        sort = sorted(nums)
        
        
        for i in range(len(sort)):
            if (i+1 in sort) == False:
                result.append(i+1)
              
        return result

This code is Time limit exceed 
The reason is sorted, i+1 in sort  => this in for loop. it needs a lot of runtime. as same as nested for loop

"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        arr = [0] * (len(nums)+1) # input nums range is 1 <= nums[i] <= n, so arr index will be 1~len(nums)+1
        # print(arr)
        for i in nums:
            arr[i] = 1
        # print(arr)
        for i in range(1,len(nums)+1):
            if arr[i] == 0:
                result.append(i)
        return result
                