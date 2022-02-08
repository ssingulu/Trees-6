# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n)
# Space: O(n) # If we include the recursion memory
class Solution(object):
    def __init__(self, low= None, high=None):
        self.ans = 0
        self.low = low
        self.high = high
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.low = low
        self.high = high
        self.helper(root)
        return self.ans
    def helper(self, node):
        if node == None:
            return
        if node.val >= self.low and node.val <= self.high:
            self.ans += node.val
        self.helper(node.left)
        self.helper(node.right)
        
