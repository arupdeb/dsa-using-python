'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104


Test cases: 
1. root : [3,4,5,1,2] , subTree: [4,1,2]
2. root : [3,4,5,1,2,null,null,null,null,0] , subTree : [4,1,2]
3. root : [1,3,1] , subTree : [1]
4. root : [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2] , subTree : [1,null,1,null,1,null,1,null,1,null,1,2]

'''

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: 
# compare each node of the larger tree to be starting of the sub-tree to compare
# time complexity : O(tree1 * tree2) = O(n2) ; Space complexity : O(1)
# runtime : 158 ms ; Memory : 14.2 MB
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None and subRoot == None:
            return True
        elif root == None or subRoot == None:
            return False

        result = self.isSameTree(root, subRoot)
        if not result:
            result = self.isSubtree(
                root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return result

    def isSameTree(self, main, sub): 

        if main == None and sub == None:
                return True
        elif main == None or sub == None:
            return False

        if main.val == sub.val:
            return self.isSameTree(main.left, sub.left) and self.isSameTree(main.right , sub.right)


# Solution 2: same approach differnt code:
# runtime: 133 ms ; Memory : 14.5 MB
# class Solution(object):
#     def isSubtree(self, root, subRoot):
#         """
#         :type root: TreeNode
#         :type subRoot: TreeNode
#         :rtype: bool
#         """

#         if not subRoot : # if subTree is null i.e it is subTree of all trees
#             return True
#         if  not root:       # if tree is null , and subTree is not null : False : order is important
#             return False 
         
#         if self.isSameTree(root, subRoot):
#             return True

#         return  self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


#     def isSameTree(self,main , sub):
            
#             if main == None and sub == None:
#                 return True
#             if main and sub and main.val == sub.val:
#                 return self.isSameTree(main.left , sub.left) and self.isSameTree(main.right , sub.right)

#             return False
                

def main():
    tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree2 = TreeNode(1)
    sol = Solution()
    print(sol.isSubtree(tree1, tree2))





if __name__ == "__main__":
    main()