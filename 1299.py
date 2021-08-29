"""
1299 -  Replace Elements with Greatest Element on Right Side

Note : range syntax 
        range(Starting number, Ending number + 1, Step) 
        ×Starting number and Step can be ommit
        ex) if we want to repeat 5 ~ 0, => range(5, -1, -1)
            if we want to repeat 5 ~ 1, => range(5, 0, -1) 
"""

class Solution(object):
    def replaceElements(self, arr):
        answer = [0] * len(arr)
        answer[-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            answer[i] = max([answer[i+1],arr[i+1]])
            
        return answer

            