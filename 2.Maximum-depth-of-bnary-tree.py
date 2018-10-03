'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class Solution:
	def maxDepth(TreeNode root):
		if root is null:
			return 0;
		int lDepth = maxDepth(root.left)
		int rDepth = maxDepth(root.right)
		return 1+(lDepth > rDepth? lDepth: rDepth)