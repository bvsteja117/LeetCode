# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(root, result):
            if not root:
                return
            
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
        
        values1 = []
        values2 = []
        inorder(root1, values1)
        inorder(root2, values2)
        merged = []
        i = j = 0
        
        while i < len(values1) and j < len(values2):
            if values1[i] <= values2[j]:
                merged.append(values1[i])
                i += 1
            else:
                merged.append(values2[j])
                j += 1
        
        while i < len(values1):
            merged.append(values1[i])
            i += 1
        
        while j < len(values2):
            merged.append(values2[j])
            j += 1
        
        return merged