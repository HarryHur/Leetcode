# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, postorder = [], []
        #stack = []
        #postorder = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            temp = stack[-1].right
            if temp is not None:
                root = temp
            else:
                temp = stack.pop()
                postorder.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    postorder.append(temp.val) 
        return postorder
                