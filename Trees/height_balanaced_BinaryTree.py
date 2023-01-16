'''
Given a binary tree, determine if it is 
height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # Solution 1: 
    # time complexity: o(n) ; space complexity : 0(n)
    # runtime: 32 ms ; memory : 18.4 MB
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = [0]
        res[0] = True
        def balance(root):
            if root == None:
                return 0
            # print(root.val)
            left  = 1 + balance(root.left)
            right = 1 + balance(root.right)
            if abs(left - right) > 1 :
                res[0] = False
            # print(left, right)
            return max(left, right)
        balance(root)
        return res[0]


def main():
    # [1,2,2,3,3,null,null,4,4]
    tree = TreeNode(1,TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),TreeNode(2))
    sol = Solution()
    print(sol.isBalanced(tree))


if __name__ == "__main__":
    main()
     
    
        

