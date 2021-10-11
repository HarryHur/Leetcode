# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
                        1
                     /     \
                    2       3
                   / \     / \
                  4   5   6   7
        '''
        
        
        if root is None:
            return []
        stack, preorder = [root],[]
        print(stack)
        while stack:
            root = stack.pop()
            preorder.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return preorder
            