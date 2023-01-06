'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# solution 1: 
# time limit exceeded. Space complexity is o(n)

# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = s.lower()
#         if not s.isalnum():
#             for i in range(len(s)):
#                 if not ((s[i] >= chr(97) and s[i] <= chr(122)) or (s[i] >= chr(48) and s[i] <= chr(57))):
#                     s = s.replace(s[i]," ")
#         s = s.replace(" ", "")
#         print(s)
#         for i in range((len(s)+1)/2):
#             if s[i] != s[-(i+1)]:
#                 return False
#         return True

