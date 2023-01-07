'''
Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# solution 1: using a stack
# time complexity : o(n) && space complexity: o(n) // worst case scenario: store all input brackets into the stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #print(s)
        openBrackets = ["(","{","["]
        closeBrackets = [")", "}", "]"]
        stack = []
        if len(s)%2 != 0 :
            return False
        else:
            for i  in range(len(s)):
                if s[i] in openBrackets:
                    stack.append(s[i])
                    # print(stack,i)
                elif len(stack) != 0 and closeBrackets.index(s[i]) == openBrackets.index(stack[len(stack)-1]):
                    stack.pop()
                    # print(stack,i)
                elif len(stack) == 0 and s[i] in closeBrackets:
                    return False
                else:
                    return False

            if len(stack) != 0 :
                # print(stack)
                return False
            else:
                return True             
                    
