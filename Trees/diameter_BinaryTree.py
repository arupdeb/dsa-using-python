'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

# solution explaination : 
# move to the depth / last node of the tree and calculate the maximun of depth of each subtree;
# then take the max left subtree and max right subtree -> add them -> to get diameter of the subtree/node
# calculate the max of diameter from each recursion of node -> return the max value

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # solution :
    # time complexity : o(n) ; space complexity = o(1)
    # runtime: 24 ms ; Memory : 16 MB
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
            
        diameter = [0]                      # define a global variable

        # using a recusive function to caluate the depth of each subtree: 
        # add the max height of sub tree and compare with the previously stored diamater: 
        # calc diamater by adding depth of left and right subtree
        def dfs(root):
            # global diameter
            if root == None:
                return -1
            leftDepth = 1 + dfs(root.left)          
            rightDepth = 1 + dfs(root.right)

            diameter[0] = max(diameter[0], leftDepth + rightDepth)          # accessing the global varibale
            return max(leftDepth, rightDepth)
        
        dfs(root)
        return diameter[0]
        

def main():
    tree  = TreeNode(1,TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    sol = Solution()
    print(sol.diameterOfBinaryTree(tree))


if __name__ == "__main__":
    main()

