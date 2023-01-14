'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None :
            return 0
        
        leftside = 1 + self.maxDepth(root.left)
        rightside = 1 + self.maxDepth(root.right)

        if leftside > rightside:
            return leftside
        else:
            return rightside


def main():
    tree = TreeNode(3)
    tree.left = TreeNode(25,TreeNode(15, TreeNode(36)), TreeNode(45))
    tree.right = TreeNode(30)
    print(Solution().maxDepth(tree))

if __name__ == "__main__":
    main()