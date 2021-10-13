'''
-----------------------------------------------
I think there is a difference between
   1. while queue is not None:
            and
   2. while queue != []:

Option 1 making runtime error.
I'm still figuring out.

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = [root]
        next_queue, carry, level = [], [], []

        
        #while queue is not None:
        while queue != []:
            for root in queue:
                carry.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
                
            level.append(carry)
            carry = []
            queue = next_queue
            next_queue = []
            
        return level
        