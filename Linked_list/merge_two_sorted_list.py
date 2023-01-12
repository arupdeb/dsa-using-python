'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
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


# solution 1: 
# time complexity: o(n) ; space complexity : o(n)
# runtime: 20 ms ; Memory: 13.6 MB

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # to avoid the edge cases of empty list input
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


def main():
    head = ListNode(3)
    head.next = ListNode(36)
    head.next.next = ListNode(76)
    # head.printList()

    head2 = ListNode(23)
    head2.next = ListNode(46)
    head2.next.next = ListNode(56)
    # head2.printList()
    sol = Solution()
    join = sol.mergeTwoLists(head, head2)
    join.printList()

if __name__ == "__main__":
    main()



