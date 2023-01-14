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

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # solution 1: recursive depth first search
    # time complexity: o(n) ; space complexity: o(1)
    # runitme: 19 ms ; memory : 16 MB
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        leftside = 1 + self.maxDepth(root.left)
        rightside = 1 + self.maxDepth(root.right)

        if leftside > rightside:
            return leftside
        else:
            return rightside


    # solution 2: Iterative BFS [ always done using queue ]: count the levels of the tree to find max height
    # time complexity : o(n) ; space complexity = o(n) - store n nodes in queue
    # runtime : 18 ms ; Memory : 16 MB
    def maxDepthBFS(self, root):
        if root == None:
            return 0

        levels = 0
        # use double edged queue from collections module
        q = collections.deque([root])

        while q:  # while there is element in queue i.e iterate each level :

            levels += 1

            # take a snapshot of queue at this length (contains elements only from one level for each while loop)
            for i in range(len(q)):
                # remove one element and replace it with it's child at the end of queue
                node = q.popleft()

                if node.left:           # if left child exist add to end of queue
                    q.append(node.left)
                if node.right:          # if right child exist add to end of queue
                    q.append(node.right)

        return levels


    # Solution 3: Iterative DFS : [only achieved using stack - emulating callstack of recusive calls]
    # we'll do pre-order traversal : easilest DFS to implement
    # time complexity o(n) ; space complexity : o(n)
    # runtime : 31 ms ; Memory : 15.8 MB
    def maxDepthIterativeDFS(self, root):

        # if root == None:      # not reuired as node will be false if root is empty
        #     return 0

        stack = [[root, 1]]  # stack of nodes, level to find the depth
        level = 0

        while stack:
            node, depth = stack.pop()               # contains two values so need to store in 2 variables

            if node:                                # if node has value/data: add left and right children and increase depth value
                level = max(level, depth)           # calculate level only if node is not null
                stack.append([node.left, depth + 1])  # add left and right element to the stack and increase depth by 1
                stack.append([node.right, depth + 1]) 
        return level




def main():
    tree = TreeNode(3)
    tree.left = TreeNode(25, TreeNode(15, TreeNode(36)), TreeNode(45))
    tree.right = TreeNode(30)
    print(Solution().maxDepth(tree))
    print("ITR BFS", Solution().maxDepthBFS(tree))
    print("ITR DFS", Solution().maxDepthIterativeDFS(tree))



if __name__ == "__main__":
    main()
