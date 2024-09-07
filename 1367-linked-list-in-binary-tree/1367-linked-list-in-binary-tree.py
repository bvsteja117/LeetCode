# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        arr, f = [], [-1]
        i, node = -1, head
        while node: 
            while i != -1 and node and node.val != arr[i]:
                i = f[i]
            i += 1
            f.append(i)
            arr.append(node.val)
            node = node.next

        def dfs(root, u):
            if not root: return False
            while u != -1 and root.val != arr[u]:
                u = f[u]
            u += 1
            if u == len(arr): return True
            return dfs(root.left, u) or dfs(root.right, u)
        return dfs(root, 0)
        