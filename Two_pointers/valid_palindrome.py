'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

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

# solution 1: not a good solution
# time limit exceeded. Space complexity is o(1)

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

# solution 2: similar approach but in a differnt way. # runtime: 141 ms
# time complexity : o(n) - space complexity o(n) // not ideal 
# class Solution(object):
#     def isPalindrome(self, s):
#         newstring = ""
#         for c in s:
#             if c.isalnum():
#                 newstring += c.lower()
#         return newstring == newstring[::-1]  // used new memory while reversing 

# solution 3: Use o(1) memory
# time complexity : o(n), space complexity is o(1)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1

        while i<j :
            if  not self.isAlphanum(s[i]):
                i+=1
                continue
            if not self.isAlphanum(s[j]):
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

    def isAlphanum(self, c):
        return ( ( chr(97) <= c <= chr(122)) or 
                    (chr(48) <= c <= chr(57)) or 
                    ( chr(65) <= c <= chr(90)) )


# alternate solution takes 70 ms runtime: just changing 'if' to 'while' // 2 loops does not take o(n^2)
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         i, j = 0, len(s)-1

#         while i<j :
#             while i<j and  not self.isAlphanum(s[i]):
#                 i+=1
#             while i<j and not self.isAlphanum(s[j]):
#                 j-=1
#             if s[i].lower() != s[j].lower():
#                 return False
#             i,j = i+1, j-1
#         return True

#     def isAlphanum(self, c):
#         return ( ( chr(97) <= c <= chr(122)) or 
#                     (chr(48) <= c <= chr(57)) or 
#                     ( chr(65) <= c <= chr(90)) )
