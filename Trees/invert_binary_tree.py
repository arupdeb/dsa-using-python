'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_Pre_Order_Traversal(self):
        print(self.val)
        if self.left == None and self.right == None:
            return
        self.left.print_Pre_Order_Traversal()
        self.right.print_Pre_Order_Traversal()


class Solution(object):

    # solution 1: using recursion
    # time complexity : o(n) ; space complexity = o(1)
    # runtime : 18 ms ; Memory : 13.6 MB
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if root.left == None and root.right == None:
        #     return root
        if root == None:
            return

        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)
        # print(leftNode, rightNode)
        root.left = rightNode
        root.right = leftNode

        return root


def main():
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print("Before Inversion")
    tree.print_Pre_Order_Traversal()
    sol = Solution()
    invertedTree = sol.invertTree(tree)
    print("After Inversion")
    invertedTree.print_Pre_Order_Traversal()


if __name__ == "__main__":
    main()
