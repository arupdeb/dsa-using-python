'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # solution 1:
    # time complexity : o(p +q) = o(n), Space complexity : o(1)
    # runitme : 13 ms ; Memory: 13.4 MB
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    # [1,2,1] [1,1,2]
    tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree2 = TreeNode(1, TreeNode(1), TreeNode(2))
    sol = Solution()
    print(sol.isSameTree(tree1, tree2))

if __name__ == "__main__":
    main()
    