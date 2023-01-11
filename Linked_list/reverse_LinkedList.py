'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self):
        if self == None:
            return None
        else:
            temp = self
            while temp :
                print(temp.val)
                temp = temp.next

class Solution(object):
    # reverse a linked list using 2 pointer theory : Solution 1
    # time compexity o(n) ; Space complexity o(1); 
    # runtime: 25 ms; memory: 15.4 MB
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    # reverse a linked list using recursion: solution 2
    #time complexity o(n) ; space complexity : o(n);
    # runtime : 19 ms; memory: 18.8 MB
    def recusiveReverseList(self, head):
        if head == None or head.next == None:
            return head
        
        newhead = self.recusiveReverseList(head.next)   # recusive loop to get the last element
        head.next.next = head                           # use an example:  1 -> 4 -> 6 -> 7
        head.next = None

        return newhead
        

def main():
    head = ListNode(23)
    head.next = ListNode(46)
    head.next.next = ListNode(-76)
    head.printList()
    sol = Solution()
    # rev = sol.reverseList(head)
    # rev.printList()

    recRev = sol.recusiveReverseList(head)
    recRev.printList()

if __name__ == "__main__":
    main()
